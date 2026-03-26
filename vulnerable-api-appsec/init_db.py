import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cursor.execute("DELETE FROM users")

cursor.execute("INSERT INTO users (username, password) VALUES ('admin', '1234')")
cursor.execute("INSERT INTO users (username, password) VALUES ('teus', 'senha')")

conn.commit()
conn.close()

print("Database initialized!")