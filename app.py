from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('transactions.csv')

    # Clean
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df['Category'] = df['Category'].fillna('Uncategorized')
    df['Description'] = df['Description'].fillna('Unknown Vendor')
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date', 'Amount'])

    # Format Date
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df['Amount'] = df['Amount'].round(2)

    # Monthly Spend
    df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M').astype(str)
    monthly_data = df.groupby('Month')['Amount'].sum().round(2).sort_index()
    chart_month_labels = list(monthly_data.index)
    chart_month_values = list(monthly_data.values)

    # Category Totals
    category_data = df.groupby('Category')['Amount'].sum().round(2).sort_values(ascending=False)
    chart_cat_labels = list(category_data.index)
    chart_cat_values = list(category_data.values)

    # Flag Suspicious
    df['Suspicious'] = df.apply(lambda row: row['Amount'] > 10000 and row['Category'] != 'Credit', axis=1)
    suspicious = df[df['Suspicious']]

    # Table Preview
    table_data = df.sort_values('Date', ascending=False).head(10).to_dict(orient='records')

    return render_template(
        'index.html',
        suspicious_list=suspicious.to_dict(orient='records'),
        transactions=table_data,
        chart_month_labels=chart_month_labels,
        chart_month_values=chart_month_values,
        chart_cat_labels=chart_cat_labels,
        chart_cat_values=chart_cat_values
    )

if __name__ == '__main__':
    app.run(debug=True)
