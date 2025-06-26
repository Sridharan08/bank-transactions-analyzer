# 💸 Bank Transactions Analyzer

A web-based Python app that analyzes and visualizes your bank transaction CSV file using **Flask**, **Pandas**, and **Chart.js**. It shows monthly and category-wise spending, detects suspicious transactions, and displays interactive charts in the browser.

---

## 🚀 Features

- 📁 **CSV Cleaning**: Cleans transaction data (amounts, missing categories, invalid dates)
- 📊 **Visual Analytics**:
  - Monthly spend (bar + line chart)
  - Category-wise spend (doughnut chart)
- 🔎 **Suspicious Detection**: Flags transactions over ₹10,000
- 📋 **Recent Transactions Table**: Shows the latest 10 transactions
- 🌐 **Interactive UI**: Responsive layout styled with teal color theme

---

## 🧰 Tech Stack

| Component | Tech |
|----------|------|
| Backend  | Flask, Python, Pandas |
| Frontend | HTML, Jinja2, Chart.js, CSS |
| Visualization | Chart.js, Custom CSS |

---

## 📁 Folder Structure

bank-transactions-analyzer/
├── app.py
├── transactions.csv
├── templates/
│ └── index.html
├── static/
│ └── style.css (optional)
└── README.md

---

---

## 📄 Sample CSV Format

Make sure your CSV looks like this:

| Date       | Description       | Category  | Amount   |
|------------|-------------------|-----------|----------|
| 2025-03-01 | Amazon Purchase   | Shopping  | 3299.99  |
| 2025-03-02 | ATM Withdrawal    | Cash      | 10000.00 |
| 2025-03-03 | Credit Card Bill  | Bills     | 4500.00  |

---

## 🖥 How to Run the Project Locally

### 1. Clone the Repository

```bash
  git clone https://github.com/yourusername/bank-transactions-analyzer.git
  cd bank-transactions-analyze
```
### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
  pip install flask pandas matplotlib seaborn
```
### 4. Run the App
```bash
python app.py
```
### 5. Visit in Browser

```bash
http://127.0.0.1:5000
```
## License
MIT License



