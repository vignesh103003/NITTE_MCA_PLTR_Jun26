import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="hostel_db"
)
if connection.is_connected():
    print("Connected Successfully")
