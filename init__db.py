import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (name, password, email, address, phone, gender, birth, introduce) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('admin', '1234', 'dlrudqls99@gmail.com', 'San Marcos', '760', 'male', '2023-11-13', "Hi, I'm admin")
            )

cur.execute("INSERT INTO questionnaire (answer_1, answer_2, answer_3, comments) VALUES (?, ?, ?, ?)",
            ('admin', 'admin', 'admin', 'admin')
            )

connection.commit()
connection.close()