from Account import Account
from Banking_server import Banking_server
import time 

print("Welcome To The Banking System")
time.sleep(3)
1200
print("Please Create Your Account First ")
time.sleep(1)

class_object = Banking_server(name=input("Enter your name: "), _initial_deposit=float(input("Enter your initial deposit: ")))
print("Your Account Has Been Created ")

print(f"Your bank account uid is: {class_object.account_id}")

"\n"
while True:
    choice = user_choice = input("Enter which operation you wanna do a: deposit, b: withdraw, c: check bank balance,  d: show transaction history ")
    class_object.bank(choice)

    
