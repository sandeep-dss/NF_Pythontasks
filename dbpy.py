import mysql.connector


db = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

cursor = db.cursor()

sql = "INSERT INTO employee (name, email) VALUES (%s, %s)"
values = ("Sandeep", "sandeep@example.com")
cursor.execute(sql, values)
db.commit()
print(cursor.rowcount, "record inserted.")

sql = "SELECT * FROM employee"
cursor.execute(sql)
records = cursor.fetchall()

for record in records:
    print(record)