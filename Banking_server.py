from Account import Account
from datetime import datetime
import time
import uuid


class Banking_server(Account):
    
    def bank(self,choice):
                if choice == "1":
                    self.deposit(deposit=float(input("Enter the amount to be deposited: ")))
                elif choice == "2":
                    self.withdraw(withdraw=float(input("Enter the amount to be withdrawn: ")))
                elif choice == "3":
                    self.check_balance()
                elif choice == "4":
                    self.display_transaction_history()
                elif choice == "5":
                    self.new_account(name =  input("Enter your name :"),
                                     
                                     contact_no = int(input("Enter your contact no :")),
                                     email = input("enter your email address :"),
                                     city = input("Enter your city name :"),
                                     account_type = (input("Enter your account type from 'Saving Account', 'Current Account' :")))
                elif choice == "6":
                     print() 
                else:
                    print("Invalid Input")


    def deposit(self,deposit):
        self.initial_deposit += deposit
        self._add_transaction("Deposit",deposit)
        "\n" 
        print(f"Your transaction is completed the amount is deposited in your account the remaining balance is :{self.initial_deposit}")


    def withdraw(self,withdraw):
        if withdraw <= self.initial_deposit :
            self.initial_deposit -= withdraw 
            self._add_transaction("Deposit", withdraw)
            "\n"
            print(f"Your transaction is completed the amount is withdrawn in your account the remaining balance is :{self.initial_deposit}")
        else:
             print("invalid amount") 
        

    def check_balance(self):
        print(f"Your bank balance is: {self.initial_deposit}")


    def display_transaction_history(self):
        print("action,timestamp,amount,current_balance")
        for transaction in self.transaction_history:
            print(self.initial_deposit)

            for item in transaction.values():

                print(item, end = ",")
            print()

    def new_account(self, name, contact_no, email, city, account_type):
         self.name = name 
         self.contact_no = contact_no
         self.email = email
         self.city = city
         self. account_type = account_type
         self.new_account_id = uuid.uuid4() .int % (6**6)

         print(f"your new account has been created and your new account id is {self.new_account_id}")



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
     