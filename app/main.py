import uvicorn
import os
from fastapi import FastAPI, Depends

from app.api_v1.routers.admin_router import admin_router
from app.config.config import app_config
from app.core.auth import admin_authenticate
from api_v1.routers.file_router import file_router
from api_v1.routers.httpx_router import httpx_router

from pymongo.mongo_client import MongoClient
from app.const import MONGODB_URI


def create_app() -> FastAPI:
    app = FastAPI(
        title="test_project_api",
        docs_url="/api/test_project_api",
        openapi_url="/api",
        description="test_project_api",
        version="1.0.0",
    )

    # Маршруты
    app.include_router(
        admin_router, 
        prefix="/api/admin",
        tags=["admin"],
        dependencies=[Depends(admin_authenticate)],
    )

    app.include_router(
        file_router,
        prefix="/api/file",
        tags=["file"],
    )

    app.include_router(
        httpx_router,
        prefix="/api/test",
        tags=["get_connect"],
    )

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=False, port=app_config.APP_PORT)
