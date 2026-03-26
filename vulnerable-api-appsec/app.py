from fastapi import FastAPI, Request, File, UploadFile
import sqlite3
import jwt

app = FastAPI()

SECRET = "123456"  # segredo fraco propositalmente

# =========================
# DATABASE
# =========================
def get_db():
    return sqlite3.connect("database.db")

@app.get("/")
def home():
    return {"message": "Vulnerable API running"}

# =========================
# SQL INJECTION
# =========================
@app.get("/login")
def login(username: str, password: str):
    conn = get_db()
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    result = cursor.fetchone()
    return {"result": result}

# =========================
# IDOR
# =========================
@app.get("/user/{user_id}")
def get_user(user_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return {"data": cursor.fetchall()}

# =========================
# STORED XSS
# =========================
comments = []

@app.post("/comment")
async def comment(request: Request):
    data = await request.json()
    comments.append(data.get("comment"))
    return {"msg": "saved"}

@app.get("/comments")
def get_comments():
    return {"comments": comments}

# =========================
# JWT VULNERÁVEL
# =========================
@app.post("/login-jwt")
def login_jwt(username: str):
    token = jwt.encode({"user": username}, SECRET, algorithm="HS256")
    return {"token": token}

@app.get("/profile")
def profile(token: str):
    data = jwt.decode(token, SECRET, algorithms=["HS256"])
    return {"user": data}

# =========================
# UPLOAD INSEGURO
# =========================
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()

    filename = file.filename or "temp.txt"

    with open(filename, "wb") as f:
        f.write(content)

    return {"filename": filename}

# =========================
# ADMIN SEM AUTENTICAÇÃO
# =========================
@app.get("/admin")
def admin():
    return {"secret": "admin panel - no auth"}