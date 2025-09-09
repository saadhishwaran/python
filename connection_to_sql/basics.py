
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Testdb")
cursor.execute("USE Testdb")
cursor.execute("CRESTE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), email VARCHAR(30),)""")
cursor.execute("INSERT INTO users(name, email) VALUES(%s, %s),('Aadhishwaran','Aashi@gmail.com'))")
conn.commit()