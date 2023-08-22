import uvicorn
from fastapi import FastAPI, Depends

from app.api_v1.routers import admin_router
from app.config import app_config
from app.core.auth import admin_authenticate


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

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=False, port=app_config.APP_PORT)
