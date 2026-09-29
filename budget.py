import expense

monthly_budget = 0


def set_budget():
    global monthly_budget

    print("\n--- SET BUDGET ---")

    while True:
        try:

            budget = float(input("Enter your monthly budget: "))

            if budget > 0:

                monthly_budget = budget

                print("Budget set to Rs", monthly_budget)

                break

            else:
                print("Budget must be greater than 0.")

        except ValueError:
            print("Please enter a valid amount.")


def check_budget():

    print("\n--- BUDGET STATUS ---")

    if monthly_budget == 0:
        print("Budget not set yet.")
        return

    total = 0

    for item in expense.expenses:
        total = total + item["amount"]

    remaining = monthly_budget - total

    print("Budget:", monthly_budget)
    print("Spent:", total)
    print("Remaining:", remaining)

    if remaining < 0:
        print("You went over budget by", abs(remaining))
