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
    choice = user_choice = input("Enter which operation you wanna do  (1: Deposit, 2: Withdraw, 3: Check Bank Balance,  4: Show Transaction History , 5: Create a New Account           6:Exit the banking system ) :")
    class_object.bank(choice)   
    if choice == "6":
         print("Thanks for visiting the Banking System Have a nice day ")
         break
    
    
