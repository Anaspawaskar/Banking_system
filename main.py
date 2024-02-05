"""main file where every thing
"""
import time
from banking_server import BankingServer


print("Welcome To The Banking System")
time.sleep(3)

print("Please Create Your Account First ")
time.sleep(1)

class_object = BankingServer(
    name=input("Enter your name: "),
    initial_deposit=float(input("Enter your initial deposit: ")),
)
print("Your Account Has Been Created ")

print(f"Your bank account uid is: {class_object.account_id}")


while True:
    dirc = {
        1: "deposit",
        2: "Withdraw",
        3: "check_bank_balance",
        4: "show transaction history",
        5: "create a new account",
        6: "to check the new account number",
    }
    choice = user_choice = input(dirc)

    class_object.bank(choice)
    if choice == "6":
        print("Thanks for visiting the Banking System Have a nice day ")
        break
