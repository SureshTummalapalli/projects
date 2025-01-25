# This is a basic banking system implementation in Python that allows users to create accounts, log in, deposit and withdraw funds, check balances, and view mini statements. The system consists of two classes: Account and BankingSystem.

# -----------BANKING SYSTEM-------------
class Account:
    def __init__(self, username, password, balance=0):
        # Initialize account with username, password, and balance.
        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = []  # Store transaction history

    def deposit(self, amount):
        # Add the deposit amount to the balance and record the transaction.
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"\nAmount deposited: {amount}\nTotal Balance: {self.balance}")

    def withdraw(self, amount):
        # Deduct the withdrawal amount if sufficient balance exists, else notify.
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print(f"\nAmount withdrawn: {amount}\nRemaining Balance: {self.balance}")
        else:
            print("Insufficient balance")

    def get_mini_statement(self):
        # Print account details and transaction history.
        print(f"\n--- Mini Statement ---\nUsername: {self.username}\nBalance: {self.balance}")
        print("Transactions:", *self.transactions, sep="\n")


class BankingSystem:
    def __init__(self):
        # Store accounts with usernames as keys.
        self.accounts = {}

    def create_account(self, username, password):
        # Create a new account if the username is unique.
        if username in self.accounts:
            print("Username already exists")
        else:
            self.accounts[username] = Account(username, password)
            print("\nAccount created successfully\n-------Welcome to PYTHON Bank-------")

    def login(self, username, password):
        # Validate username and password for login.
        account = self.accounts.get(username)
        if account and account.password == password:
            print("Login Success...")
            return account
        print("Invalid username or password")
        return None


def display_menu(options):
    # Display a menu and return the user's choice.
    print("\n".join(options))
    return input("Enter your choice: ")


def main():
    bank = BankingSystem()
    main_menu = ["\n1. Create account", "2. Login", "3. Exit"]

    while True:
        choice = display_menu(main_menu)

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            bank.create_account(username, password)

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            account = bank.login(username, password)

            if account:
                sub_menu = [
                    "\n----- PYTHON Bank -----",
                    "1. Deposit",
                    "2. Withdraw",
                    "3. Check Balance",
                    "4. Mini Statement",
                    "5. Logout",
                ]
                while True:
                    sub_choice = display_menu(sub_menu)

                    if sub_choice == '1':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)

                    elif sub_choice == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)

                    elif sub_choice == '3':
                        print(f"Current balance: {account.balance}")

                    elif sub_choice == '4':
                        account.get_mini_statement()

                    elif sub_choice == '5':
                        print("\n-------- THANK YOU, VISIT AGAIN --------")
                        break

                    else:
                        print("Invalid choice")

        elif choice == '3':
            print("\n------ THANK YOU ------")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()