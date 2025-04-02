from database import db_query  # Import only db_query (avoid using import *)
import random
from bank import Bank

def SignUp():
    while True:
        username = input("Create Username: ")

        # Check if username exists in the database
        temp = db_query(f"SELECT username FROM customers WHERE username = '{username}'")

        if temp:
            print("Username Already Exists. Try Again.")
            SignUp()  # Ask for username again
        else:
            print("Username is Available! Please Proceed")
            break  # Exit loop once a valid username is provided

    password = input("Enter your password: ")
    name = input("Enter your name: ") 
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    
    while True:
    # Corrected account number range (8-digit number)
        account_number = int(random.randint(10000000, 99999999))
        temp = db_query(f"SELECT account_number FROM customers WHERE account_number ='{account_number}'")

        if temp:
            continue
        else:
            print("Your Account Number", account_number)
            break
    cobj = Customer(username, password, name,  age, city,account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()
    
def SignIn():
    username =input("Enter Username: ")
    temp = db_query(f"SELECT username From customers where username ='{username}'")
    if temp:
        while True:
            password =input("Welcome {username.capitalize()} Enter password")
            temp = db_query(f"SELECT password From customers where username ='{username}'")
            ## print(temp[0][0])
            if temp[0][0] == password:
                print("Sign IN sussesfully")
                return username
                
            else:
                print("Wrong password try again")
                continue
    else:
        print("Enter correct username")
        SignIn()
        
