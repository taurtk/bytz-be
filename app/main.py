from fastapi import FastAPI, Depends
from app.routes import router as api_router
from app.middleware import add_cors_middleware
import os

app = FastAPI()
add_cors_middleware(app)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)
