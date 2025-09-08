import mysql.connector

mydb = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'SkillSavvy@25',
    database = 'students'
)
print('connection successful')

cursor = mydb.cursor()
cursor.execute('SELECT * FROM students_data')
for data in cursor.fetchall():
    print(data)

cursor.close()
mydb.close()