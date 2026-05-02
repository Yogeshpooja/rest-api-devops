from fastapi import APIRouter, Body
from app.database.db import get_db_connection
from app.services.auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/users", tags=["Users API"])



@router.get("/")
def get_all_users():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, name FROM users;")
        rows = cur.fetchall()

        cur.close()
        conn.close()

        users = [{"id": r[0], "name": r[1]} for r in rows]

        return {"users": users}

    except Exception as e:
        return {"error": str(e)}



@router.post("/register")
def register_user(name: str = Body(...), password: str = Body(...)):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        hashed = hash_password(password)

        cur.execute(
            "INSERT INTO users (name, password) VALUES (%s, %s)",
            (name, hashed)
        )
        conn.commit()

        cur.close()
        conn.close()

        return {"message": "User registered successfully"}

    except Exception as e:
        return {"error": str(e)}



@router.post("/login")
def login_user(name: str = Body(...), password: str = Body(...)):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE name=%s", (name,))
        user = cur.fetchone()

        cur.close()
        conn.close()

        if not user:
            return {"error": "User not found"}

        if not verify_password(password, user[2]):
            return {"error": "Invalid password"}

        token = create_access_token({"sub": user[1]})

        return {"access_token": token}

    except Exception as e:
        return {"error": str(e)}
