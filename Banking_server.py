"""banking_server has created here
"""

from datetime import datetime
from account import Account


class BankingServer(Account):
    """banking_server is creating

    Args:
        Account (_type_): _description_
    """

    def bank(self, choice):
        """
        this is the banking server where user have the operatio  to perform

        Args:
            choice (_type_): string
        """
        if choice == "1":
            self.deposit(deposit=float(input("Enter the amount to be deposited: ")))
        elif choice == "2":
            self.withdraw(withdraw=float(input("Enter the amount to be withdrawn: ")))
        elif choice == "3":
            self.check_balance()
        elif choice == "4":
            self.display_transaction_history()
        elif choice == "5":
            NewAccount(
                name=input("Enter your name :"),
                contact_no=int(input("Enter your contact no :")),
                email=input("enter your email address :"),
                city=input("Enter your city name :"),
            )
        elif choice == "6":
            print()

        else:
            print("Invalid Input")

    def deposit(self, deposit):
        """
        here depositing the amount


        Args:
            deposit (_type_): _description_
        """

        self.initial_deposit += deposit
        self._add_transaction("Deposit", deposit)

        print(
            f"Your transaction is completed and remaining balance is :{self.initial_deposit}"
        )

    def withdraw(self, withdraw):
        """
        withdraw method to withdraw the amount
        """

        if withdraw <= self.initial_deposit:
            self.initial_deposit -= withdraw
            self._add_transaction("deposit", withdraw)

            print(
                f"Your transaction is completed and remaining balance is :{self.initial_deposit}"
            )
        else:
            print("invalid amount")

    def check_balance(self):
        """
        here user can check his bank balance
        """

        print(f"Your bank balance is: {self.initial_deposit}")

    def display_transaction_history(self):
        """
        here is displaying transaction history
        """

        print("action,timestamp,amount,current_balance")
        for transaction in self.transaction_history:
            print(self.initial_deposit)

            for item in transaction.values():

                print(item, end=",")
            print()

    def _add_transaction(self, action, amount):
        """
        here printing the transaction


        Args:
            action (_type_): int
            amount (_type_): int
        """

        timestamp = datetime.now().strftime("%d %b %Y %H:%M:%S")
        current_balance = self.initial_deposit
        transaction = {
            "Action": f"{action}",
            "Timestamp": f"{timestamp}",
            "Amount": f"{amount}",
            "Current Balance": f"{current_balance}",
        }
        self.transaction_history.append(transaction)


class NewAccount:
    """here the new account can be added"""

    def __init__(self, name, contact_no, email, city):
        """here user can be create a new account

        Args:
            name (type): string
            contact_no (type): int
            email (type): mix
            city (type): string
            account_type (type): int
        """

        self.name = name
        self.contact_no = contact_no
        self.email = email
        self.city = city

    def new(self):
        """new tympss"""

    def new1(self):
        """new tympss"""
