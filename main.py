from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"My first deployment is working"}
@app.get("/health")
def health():
    return {"status":"ok"}