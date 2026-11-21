from fastapi import FastAPI
from app.routers import addition,subtraction,multiplication


app = FastAPI(
    title="Addition API",
    description="A simple FastAPI addition endpoint",
    version="1.0.0"
)

app.include_router(addition.router)
app.include_router(subtraction.router)
app.include_router(multiplication.router)   


@app.get("/")
def home():
    return {"message": "Welcome to Addition API"}