import expense
import category
import budget


def display_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expense")
    print("4. Category-wise Summary")
    print("5. Search by Category")
    print("6. Search by Date")
    print("7. Monthly Summary")
    print("8. Set Monthly Budget")
    print("9. Check Budget")
    print("10. Delete Expense")
    print("11. Exit")


# Load expenses when program starts
expense.load_expenses()


# Main program
while True:

    display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        expense.add_expense()

    elif choice == "2":
        expense.view_expenses()

    elif choice == "3":
        expense.total_expense()

    elif choice == "4":
        category.category_summary()

    elif choice == "5":
        expense.search_category()

    elif choice == "6":
        expense.search_date()

    elif choice == "7":
        expense.monthly_summary()

    elif choice == "8":
        budget.set_budget()

    elif choice == "9":
        budget.check_budget()

    elif choice == "10":
        expense.delete_expense()

    elif choice == "11":
        print("Bye! Your expenses are saved.")
        break

    else:
        print("Invalid choice, try again.")
