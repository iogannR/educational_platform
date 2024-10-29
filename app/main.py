import uvicorn
from fastapi import FastAPI
from dishka.integrations.fastapi import setup_dishka

from app.api import router as api_router
from app.infrastructure.dependencies import create_async_container
from app.infrastructure.config import settings
    

def create_app() -> FastAPI:
    app: FastAPI = FastAPI()
    app.include_router(api_router)
    return app


def create_production_app() -> FastAPI:
    app = create_app()
    container = create_async_container(url=str(settings.db.url))
    setup_dishka(container, app)
    return app


if __name__ == "__main__":
    uvicorn.run("app.main:create_production_app", factory=True, reload=True)