import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
    )
    if mydb.is_connected():
        print("Connection established")
except mysql.connector.Error as err:
    print(f"Error: {err}")

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS school_db")
cursor.execute("USE school_db") 

cursor.execute("""
CREATE TABLE IF NOT EXISTS students_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(10)
)
""")
cursor.execute("INSERT INTO students_data (name, age, grade) VALUES ('Alice', 14, '8th')")
cursor.execute("INSERT INTO students_data (name, age, grade) VALUES ('Bob', 15, '9th')")

mydb.commit()

cursor.execute("SELECT * FROM students_data")
for data in cursor.fetchall():
    print(data)

cursor.close()
mydb.close()