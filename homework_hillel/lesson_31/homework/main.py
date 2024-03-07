import sqlite3
import pprint

conn = sqlite3.connect('cars.db', isolation_level=None)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cars
                  (id INTEGER PRIMARY KEY,
                   name TEXT,
                   brand TEXT,
                   year INTEGER,
                   price REAL)''')

# cursor.execute("DELETE FROM cars")

cursor.executemany('INSERT INTO cars (name, brand, year, price) VALUES(?, ?, ?, ?);', [
    ('Honda Civic', 'Honda', 2018, 22000),
    ('Toyota Corolla', 'Toyota', 2019, 23000),
    ('Ford Mustang', 'Ford', 2020, 35000)
])

result = cursor.execute("select * from cars;")
pprint.pprint(list(result))

conn.close()
