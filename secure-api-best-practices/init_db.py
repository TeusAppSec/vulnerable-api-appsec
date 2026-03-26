import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

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

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", hash_password("1234")))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("teus", hash_password("senha")))

conn.commit()
conn.close()

print("Secure database initialized!")