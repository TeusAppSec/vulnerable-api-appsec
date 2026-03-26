from fastapi import FastAPI, HTTPException
import sqlite3
import hashlib

app = FastAPI()

def get_db():
    return sqlite3.connect("database.db")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.get("/")
def home():
    return {"message": "Secure API running"}

@app.post("/login")
def login(username: str, password: str):
    conn = get_db()
    cursor = conn.cursor()

    hashed = hash_password(password)

    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, hashed))

    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id < 1:
        raise HTTPException(status_code=400, detail="Invalid ID")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, username FROM users WHERE id = ?", (user_id,))
    return {"data": cursor.fetchall()}