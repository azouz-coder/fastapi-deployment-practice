from fastapi import FastAPI
import os
from sqlalchemy import create_engine, text
app = FastAPI()
DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is missing")
DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
engine = create_engine(DATABASE_URL)
with engine.begin() as connection:
    connection.execute(text("""CREATE TABLE IF NOT EXISTS visits (
        id SERIAL PRIMARY KEY,
        visit_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""))
@app.get("/health")
def health():
    return {"status":"ok"}
@app.get("/db-health")
def db_health():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"database":"connected"}
@app.post("/visits")
def create_visit():
    with engine.begin() as connection:
        result = connection.execute(text("INSERT INTO visits DEFAULT VALUES RETURNING id"))
        visit_id = result.scalar_one()
    return {"visit_id": visit_id}
@app.get("/visits")
def get_visits():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT COUNT(*) FROM visits"))
        visit_count = result.scalar_one()
    return {"visit_count": visit_count}


@app.get("/")
def home():
    return {
        "message": "FastAPI is running",
        "version": "2.0"
    }