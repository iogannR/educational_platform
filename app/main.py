import uvicorn
from fastapi import FastAPI

from app.api import router as api_router
from app.infrastructure.container import Container


def create_app() -> FastAPI:
    app = FastAPI(title="Educatoinal Platform v1")
    container = Container()
    app.container = container
    app.include_router(api_router, prefix="/api")
    return app


if __name__ == "__main__":
    uvicorn.run(
        "app.main:create_app",
        host="localhost",
        port=8000, 
        reload=True, 
        factory=True,
    )