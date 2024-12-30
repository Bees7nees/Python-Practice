'''
#* Bank Application

The "Bank Application" is a Python program that simulates basic banking operations.
It allows users to create accounts, log in, check balances, deposit and withdraw money, and transfer funds to other accounts.

Key Features:

    * Create Account: Users can create a new bank account by providing a unique username and password. Passwords are securely hashed using the SHA-256 algorithm before storage.
    * Login: Account holders can log in with their usernames and passwords to access their accounts.
    * Check Balance: Users can check their account balances.
    * Deposit: Account holders can deposit money into their accounts.
    * Withdraw: Users can withdraw money from their accounts, provided they have sufficient funds.
    * Transfer: Account holders can transfer money to other accounts, ensuring secure fund transfer.

Project Structure:

    * The program uses an SQLite database to store account information, including usernames, hashed passwords, and account balances.
    * User passwords are securely hashed using the SHA-256 algorithm before storage to enhance security.
    * It includes a BankApp class that encapsulates the functionality of the application, making it organized and easy to maintain.

Why This Project?
    This project serves as a practical exercise for intermediate Python programmers. It covers the following fundamental concepts:
    * Working with databases
    * User authentication
    * Class-based application structure
'''