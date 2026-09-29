FILE_NAME = "expenses"
expenses = []


def load_expenses():
    global expenses
    expenses = []

    try:
        file = open(FILE_NAME, "r")
    except:
        return

    lines = file.readlines()
    file.close()

    for i in range(1, len(lines)):
        line = lines[i].strip()

        if line == "":
            continue

        parts = line.split(",")

        expense = {
            "date": parts[0],
            "category": parts[1],
            "amount": float(parts[2]),
            "description": parts[3]
        }

        expenses.append(expense)


def save_expenses():
    file = open(FILE_NAME, "w")

    file.write("date,category,amount,description\n")

    for expense in expenses:
        line = (
            expense["date"] + ","
            + expense["category"] + ","
            + str(expense["amount"]) + ","
            + expense["description"] + "\n"
        )

        file.write(line)

    file.close()


def add_expense():
    print("\n--- ADD EXPENSE ---")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Please enter a valid amount.")

    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    save_expenses()

    print("Expense added!")


def view_expenses():
    print("\n--- ALL EXPENSES ---")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    n = 1

    for expense in expenses:
        print(
            n,
            expense["date"],
            expense["category"],
            "Rs",
            expense["amount"],
            expense["description"]
        )

        n = n + 1


def total_expense():
    print("\n--- TOTAL EXPENSE ---")

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total spent: Rs", total)


def search_category():
    print("\n--- SEARCH BY CATEGORY ---")

    search = input("Enter category to search: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == search.lower():

            print(
                expense["date"],
                expense["category"],
                "Rs",
                expense["amount"],
                expense["description"]
            )

            found = True

    if found == False:
        print("No expense found.")


def search_date():
    print("\n--- SEARCH BY DATE ---")

    search = input("Enter date (DD-MM-YYYY): ")

    found = False

    for expense in expenses:
        if expense["date"] == search:

            print(
                expense["date"],
                expense["category"],
                "Rs",
                expense["amount"],
                expense["description"]
            )

            found = True

    if found == False:
        print("No expense found.")


def monthly_summary():
    print("\n--- MONTHLY SUMMARY ---")

    month = input("Enter month and year (MM-YYYY): ")

    total = 0
    found = False

    for expense in expenses:

        date = expense["date"]

        if len(date) == 10:

            expense_month = date[3:10]

            if expense_month == month:
                total = total + expense["amount"]
                found = True

    if found:
        print("Total for", month, ": Rs", total)
    else:
        print("No expenses found for this month.")


def delete_expense():
    print("\n--- DELETE EXPENSE ---")

    if len(expenses) == 0:
        print("Nothing to delete.")
        return

    view_expenses()

    while True:
        try:
            num = int(input("Enter expense number to delete: "))

            if num >= 1 and num <= len(expenses):

                expenses.pop(num - 1)

                save_expenses()

                print("Deleted!")

                break

            else:
                print("Invalid number.")

        except ValueError:
            print("Please enter a valid number.")
