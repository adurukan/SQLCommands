import mysql.connector
from datetime import datetime
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="0631",
    database="1database"
)
mycursor = db.cursor()
# mycursor.execute("CREATE DATABASE 1database")

# ---------------------------------- #
# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
'''
mycursor.execute("DESCRIBE Person")

for x in mycursor:
    print(x)
'''
# ---------------------------------- #
'''
mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)", ("maxim", 33))
db.commit()
mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print(x)
'''
# ---------------------------------- #
'''
#mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M','F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ("KILLIAN", datetime.now(), "M"))
#db.commit()

#mycursor.execute("SELECT id,name FROM Test WHERE gender = 'M' ORDER BY id DESC")
#for x in mycursor:
#    print(x)

#mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")

#mycursor.execute("DESCRIBE Test")
#for x in mycursor:
#    print(x)

#mycursor.execute("ALTER TABLE Test DROP food")
#mycursor.execute("DESCRIBE Test")
#for x in mycursor:
#    print(x)

#mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")
#mycursor.execute("DESCRIBE Test")
#for x in mycursor:
#    print(x)
'''

'''
Foreign Keys are allowing you to refer to another table.
Users Table - Scores Table
Parent Table - Child Table
Many to One
One to Many
'''



