from fastapi import FastAPI
from app.routes import user   

app = FastAPI()

app.include_router(user.router)   

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "API is running successfully"
    }

@app.get("/health")
def health():
    return {"status": "OK"}
