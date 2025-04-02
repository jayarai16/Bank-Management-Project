# Database Management 
import psycopg2 as psy

# Database Connection Function
def connect_db():
    try:
        mydb = psy.connect(
            dbname="bank",
            user="postgres",
            password="password",
            host="localhost",
            port="5432"
        )
        print("Database Connected Successfully!")
        return mydb
    except Exception as e:
        print("Error:", e)
        return None  # Return None if connection fails

# Function to execute queries
def db_query(query, params=None, fetch=False):
    mydb = connect_db()
    if mydb is None:
        return None  # Exit if database connection fails

    cursor = mydb.cursor()
    try:
        cursor.execute(query, params if params else ())
        if fetch:
            return cursor.fetchall()
        mydb.commit()
        print("Query Executed Successfully!")
    except Exception as e:
        print("Error executing query:", e)
    finally:
        cursor.close()
        mydb.close()

# Function to create the customers table
def create_customer_table():
    query = '''
        CREATE TABLE IF NOT EXISTS customers (
            username VARCHAR(20),
            password VARCHAR(20),
            name VARCHAR(20),
            age INTEGER,
            city VARCHAR(20),
            balance INTEGER NOT NULL,
            account_number INTEGER NOT NULL,
            
            status BOOLEAN
        )
    '''
    db_query(query)

# Main function
def main():
    create_customer_table()

if __name__ == "__main__":
    main()


