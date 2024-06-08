import mysql.connector
from mysql.connector import errorcode
import pandas as pd

# MySQL server connection parameters
config = {
    'user': 'username',
    'password': 'password',
    'host': 'localhost'
}


csv_file_path = '/Users/apple/Documents/python/research2.csv'


conn = None
cursor = None

try:
 
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

  
    cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
    print("Database 'mydatabase' created successfully.")

   
    config['database'] = 'mydatabase'
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    df = pd.read_csv(csv_file_path)

 
    columns = df.columns
    create_table_query = f"CREATE TABLE IF NOT EXISTS mytable ({', '.join([f'{col} TEXT' for col in columns])})"
    cursor.execute(create_table_query)
    print("Table 'mytable' created successfully.")

  # insert into rows
    for _, row in df.iterrows():
        sql = f"INSERT INTO mytable ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in columns])})"
        cursor.execute(sql, tuple(row))
    
   
    conn.commit()
    print("Data inserted successfully into 'mytable'.")

   
    cursor.execute("SELECT COUNT(*) FROM mytable")
    count = cursor.fetchone()[0]
    print(f"Number of rows in 'mytable': {count}")

    
    cursor.execute("SELECT * FROM mytable")
    rows = cursor.fetchall()
    
    print("Data in 'mytable':")
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
   
    if cursor:
        cursor.close()
    
    if conn:
        conn.close()