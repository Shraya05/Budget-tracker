import os
import json

FILE_NAME = "budget_data.json"

def load_data():
    """Load budget data from a file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {"balance": 0.0, "transactions": []}

def save_data(data):
    """Save budget data to a file."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_income(data, amount, description):
    """Add income to the budget tracker."""
    data["balance"] += amount
    data["transactions"].append({"type": "Income", "amount": amount, "description": description})
    print(f"Added income of ${amount:.2f} with description: '{description}'.")

def add_expense(data, amount, description):
    """Add an expense to the budget tracker."""
    if amount > data["balance"]:
        print("Error: Insufficient funds! Cannot add this expense.")
        return
    data["balance"] -= amount
    data["transactions"].append({"type": "Expense", "amount": amount, "description": description})
    print(f"Added expense of ${amount:.2f} with description: '{description}'.")

def view_balance(data):
    """View the current balance."""
    print(f"\nCurrent Balance: ${data['balance']:.2f}\n")

def view_transactions(data):
    """View all transactions."""
    if not data["transactions"]:
        print("\nNo transactions recorded yet.")
        return
    print("\nTransaction History:")
    print("-" * 40)
    for i, transaction in enumerate(data["transactions"], start=1):
        print(f"{i}. [{transaction['type']}] ${transaction['amount']:.2f} - {transaction['description']}")
    print("-" * 40)

def main():
    print("Welcome to the Personal Budget Tracker!")
    data = load_data()

    while True:
        print("\nMenu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter income amount: "))
                description = input("Enter income description: ")
                add_income(data, amount, description)
            except ValueError:
                print("Invalid input! Please enter a numeric value for the amount.")
        elif choice == "2":
            try:
                amount = float(input("Enter expense amount: "))
                description = input("Enter expense description: ")
                add_expense(data, amount, description)
            except ValueError:
                print("Invalid input! Please enter a numeric value for the amount.")
        elif choice == "3":
            view_balance(data)
        elif choice == "4":
            view_transactions(data)
        elif choice == "5":
            save_data(data)
            print("Goodbye! Your data has been saved.")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
