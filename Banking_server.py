from Account import Account
from datetime import datetime
import time


class Banking_server(Account):
    
    def bank(self,choice):
                if choice == "a":
                    self.deposit(deposit=float(input("Enter the amount to be deposited: ")))
                elif choice == "b":
                    self.withdraw(withdraw=float(input("Enter the amount to be withdrawn: ")))
                elif choice == "c":
                    self.check_balance()
                elif choice == "d":
                    self.display_transaction_history()
                else:
                    print("Invalid Input")
    def deposit(self,deposit):
        self.initial_deposit += deposit
        self._add_transaction("Deposit",deposit)
        "\n" 
        print(f"Your transaction is completed the amount is deposited in your account the remaining balance is :{self.initial_deposit}")


    def withdraw(self,withdraw):
        self.initial_deposit -= withdraw if withdraw <= self.initial_deposit else "Insufficient Balance"
        self._add_transaction("Deposit", withdraw)
        "\n"
        print(f"Your transaction is completed the amount is deposited in your account the remaining balance is :{self.initial_deposit}")

    def check_balance(self):
        print(f"Your bank balance is: {self.initial_deposit}")


    def display_transaction_history(self):
        print("action,timestamp,amount,current_balance")
        for transaction in self.transaction_history:
            print(self.initial_deposit)

            for item in transaction.values():

                print(item, end = ",")
            print()

    def _add_transaction(self, action, amount):
        timestamp = datetime.now().strftime("%d %b %Y %H:%M:%S")
        current_balance = self.initial_deposit
        transaction = {
            "Action": f"{action}",
            "Timestamp": f"{timestamp}",
            "Amount":  f"{amount}",
            "Current Balance": f"{current_balance}"
        }
        self.transaction_history.append(transaction)
     