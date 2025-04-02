from register import *
from bank import *
from database import *
status = False

print(" Welcome to My Banking Project")

while True:
    try:
        register = int(input("1. SignUp\n"
                             "2. SignIn"))
        if register ==1 or register ==2:
            if register == 1:
                SignUp()
            if register == 2:
                SignIn()
                status = True
                break
        else:
            print("Please Enter valid input from options")
        
    except ValueError:
        print("Invalid Input Try Again with numbers")
        
account_number = db_query("SELECT account_number FROM customers WHERE username ='{user}' ")        

while status:
    print(f"Welcome {user.capitalize()} choose Your Banking Service\n")
    try:
        facility = int(input("1. Balance Enquiry\n"
                             "2. Cash Deposit\n"
                             "3. Cash Withdraw\n"
                             "4. Fund Transfer\n"))
        if facility >= 1 or facility <= 4:
            if facility == 1:
                bobj = Bank(user, account_number[0][0])
                bobj.balanceequiry()
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter amount to Deposit"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter valid input ie. Number")
                        continue
                
            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter amount to Deposit"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter valid input ie. Number")
                        continue
                    
                amount = int(input("Enter amount to withdraw"))
                bobj = Bank(user, account_number[0][0])
                bobj.withdraw(2000)
                
            elif facility == 4:
                while True:
                    try:
                        receiver = int(input("Enter Reciver account number"))
                        amount = int(input("Enter Money to transfer"))

                        bobj = Bank(user, account_number[0][0])
                        bobj.fundtransfer(receive,amount)
                        mydb.commit()
                        status = False

                    except ValueError:
                        print("Enter valid input ie. Number")
                        continue
                
        else:
            print("Please Enter valid input from options")
            continue
        
    except ValueError:
        print("Invalid Input Try Again with numbers")  
        continue      
    
    