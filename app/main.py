from fastapi import FastAPI
from app.db import get_db_connection

app = FastAPI()

@app.get("/")
def home():
    return {
    "status": "success",
    "message": "API is running successfully"
}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/users")
def get_users():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users;")
        users = cur.fetchall()
        cur.close()
        conn.close()
        return {"data": users}
    except Exception as e:
        return {"error": str(e)}
