💰 Expense Tracker
📌 Overview

Expense Tracker is a simple command-line Python application used to record and manage daily expenses.

It allows users to add, view, search, delete, and summarize expenses. It also includes a monthly budget feature.

The project is divided into separate Python files to keep the code simple and organized.

🚀 Features

➕ Add expenses

📋 View all expenses

💰 Calculate total expenses

📊 Category-wise summary

🔍 Search by category or date

🗓️ Monthly expense summary

💵 Set and check monthly budget

🗑️ Delete expenses

💾 Save and load expenses from a file

🛠️ Technologies Used

Python – Main programming language

File Handling – Used to store expense data

Lists and Dictionaries – Used to manage expense information

Modules and Imports – Used to divide the program into multiple files

Assert – Used for basic testing

📂 Project Structure
ExpenseTracker/
│
├── main.py          # Main program and menu
├── expense.py       # Expense-related functions
├── category.py      # Category-related functions
├── budget.py        # Budget-related functions
├── test.py          # Basic tests
├── README.md        # Project documentation
└── expenses         # Expense data file

🧠 How It Works

The user selects an option from the main menu.

The required function is then called from the respective Python file.

Expenses are stored in the expenses file and loaded when the program starts.

The project is divided into:

expense.py → Expense operations

category.py → Category summary

budget.py → Budget operations

main.py → Main menu and program flow

🧪 Testing

The project includes a simple test.py file using Python assert statements.

It tests basic operations such as expense calculations, category totals, budget calculations, and deleting expenses.

Run the tests using:

python test.py

▶️ How to Run

Make sure Python 3 is installed.

Run the main program:

python main.py


To run the tests:

python test.py

⚠️ Limitations

The application is command-line based.

Expenses are stored in a simple file instead of a database.

The monthly budget is not saved permanently.

📈 Future Enhancements

📊 Add expense charts and graphs

🗄️ Use a database for storage

✏️ Add an edit expense option

💵 Add income tracking

🖥️ Add a graphical user interface

📤 Add CSV/Excel report export

🎯 Learning Outcomes

This project helped me practice:

Python functions

Lists and dictionaries

Loops and conditions

File handling

Exception handling

Modules and imports

Basic testing using assert

👨‍💻 Author

Krishna Mishra