import pandas as pd
from datetime import datetime
import os


filename = 'expenses.csv'


if not os.path.exists(filename):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(filename, index=False)


def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if date == "":
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (e.g., Food, Travel, Recharge): ")
    try:
        amount = float(input("Enter amount spent: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return

    new_entry = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
    df = pd.read_csv(filename)
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(filename, index=False)
    print("✅ Expense added successfully!\n")


def view_summary():
    df = pd.read_csv(filename)

    if df.empty:
        print("No expenses found.")
        return

    try:
        # Let pandas automatically detect different date formats
        df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=False, errors='coerce')
    except Exception as e:
        print("Error parsing dates:", e)
        return

    print("\nTotal Expenses: ₹", df["Amount"].sum())

    print("\nCategory-wise Summary:")
    print(df.groupby("Category")["Amount"].sum())

    print("\nDate-wise Summary:")
    print(df.groupby("Date")["Amount"].sum())




def main():
    while True:
        print("\n📘 Student Daily Expense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("👋 Exiting. Have a great day!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
