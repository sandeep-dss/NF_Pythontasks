import sqlite3


conn = sqlite3.connect('example.db')


conn.execute('''CREATE TABLE IF NOT EXISTS employees
             (id INT PRIMARY KEY NOT NULL,
             name TEXT NOT NULL,
             age INT NOT NULL,
             salary REAL);''')


conn.execute("INSERT INTO employees (id, name, age, salary) VALUES (1, 'John Doe', 30, 50000.0)")
conn.execute("INSERT INTO employees (id, name, age, salary) VALUES (2, 'Jane Smith', 25, 45000.0)")


conn.commit()
conn.close()