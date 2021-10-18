import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Aa123456",
    database="ProjectDB"
)

my_cursor = db.cursor()

# my_cursor.execute("CREATE TABLE Person (name VARCHAR(50), score smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
# my_cursor.execute("INSERT INTO Person (name, score) VALUES (%s,%s)", ("vik", 0))
# db.commit()

my_cursor.execute("SELECT * FROM Person")

for x in my_cursor:
    print(x)
