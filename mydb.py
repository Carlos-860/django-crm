import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    passwd = '',
)

# prepare cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE django_crm")

print("Database created successfully!")