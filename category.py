import expense


def category_summary():
    print("\n--- CATEGORY SUMMARY ---")

    if len(expense.expenses) == 0:
        print("No expenses found.")
        return

    categories = []

    for item in expense.expenses:

        if item["category"] not in categories:
            categories.append(item["category"])

    for category in categories:

        total = 0

        for item in expense.expenses:

            if item["category"].lower() == category.lower():
                total = total + item["amount"]

        print(category, ": Rs", total)
