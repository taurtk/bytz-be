from fastapi import FastAPI, Depends
from app.routes import router as api_router
from app.middleware import add_cors_middleware

app = FastAPI()
add_cors_middleware(app)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
