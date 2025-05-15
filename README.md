# 💰 Expense Tracker using Python & Pandas

This is a simple command-line **Expense Tracker** built using Python and Pandas. It allows users to:
- Add daily expenses
- View saved expenses
- Summarize total expenses by category

---

## 📌 Objectives

- Practice basic Python and Pandas programming
- Build a real-world application useful for college students
- Learn how to read/write data using CSV

---

## ⚙️ Methodology

1. **Data Entry**: User inputs expense data (date, category, amount)
2. **Data Storage**: Data is stored in a `CSV` file using Pandas
3. **Data Processing**: Summary is shown by reading and grouping the CSV data
4. **Tool Used**: Python 3 and Pandas

---

## 📊 Block Diagram

[User Input]
↓
[Python Script]
↓
[Pandas Processes Data]
↓
[CSV File ↔ Summary View]

---

## 🗃 CSV File

All expenses are saved in `expenses.csv` in the format:
- `Date` (YYYY-MM-DD)
- `Category` (like Food, Travel, etc.)
- `Amount` (in ₹)

---

## 💻 How to Run

```bash
python expense_tracker.py

📦 Requirements
Python 3.x

Pandas

Install with:
pip install pandas
📁 Project Structure
ExpenseTrackerProject/
│
├── expense_tracker.py       # Main Python file
├── expenses.csv             # Stores saved expense data
└── README.md                # Project info file
✍️ Created by
Sathya RV
