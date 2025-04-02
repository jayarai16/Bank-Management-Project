#customer detais
from database import *
class Customer:
    
    def __init__(self,username,password,name,age,city,account_number):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__account_number = account_number
    def  createuser(self):
        db_query(f"INSERT INTO customers VALUES ('{self.__username}', '{self.__password}','{self.__name}','{self.__age}','{self.__city}','{self.__account_number}',1)")
        mydb.commit()
   #     mydb = connect_db()  # Get database connection
     #   if mydb is None:
          #  print("Database connection failed!")
           # return
        
      #  cursor = mydb.cursor()  # Create a cursor object

       # query = """
       #     INSERT INTO customers (username, password, name, age, city, account_number, status)
        #    VALUES (%s, %s, %s, %s, %s, %s, %s)
       # """
       # values = (self.__username, self.__password, self.__name, self.__age, self.__city, 0, self.__account_number, True)
        
        #try:
'''   cursor.execute(query, values)  # Execute the query
            mydb.commit()  # Commit changes to the database
            print("User created successfully!")
        except Exception as e:
            print("Error inserting data:", e)
        finally:
            cursor.close()  # Close the cursor
            mydb.close()'''