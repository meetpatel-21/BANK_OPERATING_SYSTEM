#Problem statement:
Traditional bank account exercises in programming often lack a structured way to model real-world operations like deposits, withdrawals, interest calculation, and transaction history in a single, cohesive system.
This project addresses that gap by providing a simple command-line bank management system where users can perform core banking operations and see how their actions affect the account state in real time.

#Scope of the project:
1)Implements a single-branch, single-user-at-a-time bank account system using object-oriented programming.
2)Supports basic account lifecycle actions: creation, deposit, withdrawal, interest addition, address change, and viewing details/mini-statement.
3)Focuses on backend logic and CLI interaction only; no database, networking, or GUI is included in the current scope.
4)Designed as a learning/demo project for Python OOP and control flow, not as a production-ready banking solution.

#Target users
1)Students and beginners learning Python and object-oriented programming concepts.
2)Recruiters or reviewers evaluating basic OOP, input handling, and simple business logic in Python.
3)Educators who need a small, understandable example of a banking system for teaching purposes.

#High-level features
1)Account creation with auto-incremented account number and initialization of balance and transaction history.
2)Deposit and withdrawal operations with validation for positive amounts and sufficient balance.
3)Mini-statement showing current balance and chronological transaction history.
4)Simple interest calculation over a given rate and number of years, updating balance and logging the interest transaction.
5)Ability to update the customer address and view all account details (username, PAN ID, address, account number, balance).
6)Menu-driven command-line interface allowing continuous interaction until the user chooses to exit.
