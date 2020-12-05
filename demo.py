import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="0631",
    database="1database"
)
mycursor = db.cursor()
#mycursor.execute("CREATE DATABASE 1database")