from fastapi import FastAPI
import os
from sqlalchemy import create_engine, text
app = FastAPI()
DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is missing")
engine = create_engine(DATABASE_URL)
@app.get("/")
def home():
    return{"message":"My first deployment is working"}
@app.get("/health")
def health():
    return {"status":"ok"}
@app.get("/db-health")
def db_health():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"database":"connected"}