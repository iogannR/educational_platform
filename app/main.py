import uvicorn
from fastapi import FastAPI


def create_app():
    app = FastAPI(title="Educatoinal Platform v1")
    return app


if __name__ == "__main__":
    uvicorn.run(
        "app.main:create_app",
        host="localhost",
        port=8000, 
        reload=True, 
        factory=True,
    )