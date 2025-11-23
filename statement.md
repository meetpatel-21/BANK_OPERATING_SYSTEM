Problem statement
Traditional bank account exercises in programming often lack a structured way to model real-world operations like deposits, withdrawals, interest calculation, and transaction history in a single, cohesive system.
This project addresses that gap by providing a simple command-line bank management system where users can perform core banking operations and see how their actions affect the account state in real time.

Scope of the project
Implements a single-branch, single-user-at-a-time bank account system using object-oriented programming.

Supports basic account lifecycle actions: creation, deposit, withdrawal, interest addition, address change, and viewing details/mini-statement.

Focuses on backend logic and CLI interaction only; no database, networking, or GUI is included in the current scope.

Designed as a learning/demo project for Python OOP and control flow, not as a production-ready banking solution.

Target users
Students and beginners learning Python and object-oriented programming concepts.

Recruiters or reviewers evaluating basic OOP, input handling, and simple business logic in Python.

Educators who need a small, understandable example of a banking system for teaching purposes.

High-level features
Account creation with auto-incremented account number and initialization of balance and transaction history.

Deposit and withdrawal operations with validation for positive amounts and sufficient balance.

Mini-statement showing current balance and chronological transaction history.

Simple interest calculation over a given rate and number of years, updating balance and logging the interest transaction.

Ability to update the customer address and view all account details (username, PAN ID, address, account number, balance).

Menu-driven command-line interface allowing continuous interaction until the user chooses to exit.
