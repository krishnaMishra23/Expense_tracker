import expense
import category
import budget


# Test expense list
expense.expenses = []

expense.expenses.append({
    "date": "01-09-2026",
    "category": "Food",
    "amount": 500,
    "description": "Lunch"
})

expense.expenses.append({
    "date": "02-09-2026",
    "category": "Travel",
    "amount": 300,
    "description": "Bus"
})

print("Testing expense data...")

assert len(expense.expenses) == 2
assert expense.expenses[0]["category"] == "Food"
assert expense.expenses[0]["amount"] == 500

print("Expense test passed.")


# Test total expense
print("Testing total expense...")

total = 0

for item in expense.expenses:
    total = total + item["amount"]

assert total == 800

print("Total expense test passed.")


# Test category total
print("Testing category total...")

food_total = 0

for item in expense.expenses:
    if item["category"].lower() == "food":
        food_total = food_total + item["amount"]

assert food_total == 500

print("Category test passed.")


# Test budget
print("Testing budget...")

budget.monthly_budget = 1000

total = 0

for item in expense.expenses:
    total = total + item["amount"]

remaining = budget.monthly_budget - total

assert total == 800
assert remaining == 200

print("Budget test passed.")


# Test delete expense
print("Testing delete expense...")

expense.expenses.pop(0)

assert len(expense.expenses) == 1
assert expense.expenses[0]["category"] == "Travel"

print("Delete expense test passed.")


print()
print("All tests passed successfully!")
