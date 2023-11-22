import uvicorn
from fastapi import FastAPI, Depends
import logging

from app.config.config import app_config
from app.core.auth import admin_authenticate
from api_v1.routers.file_router import file_router
from api_v1.routers.httpx_router import httpx_router
from api_v1.routers.admin_router import admin_router

logging_level = None
match app_config.LOGGING_LEVEL:
    case "INFO": app_config.LOGGING_LEVEL = logging.INFO
    case "WARNING": app_config.LOGGING_LEVEL = logging.WARNING
    case "ERROR": app_config.LOGGING_LEVEL = logging.ERROR
    case "CRITICAL": app_config.LOGGING_LEVEL = logging.CRITICAL

logging.basicConfig(level=logging_level, filename="py_log.log",
                    format="%(asctime)s - %(levelname)s - %(message)s")

# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")


def create_app() -> FastAPI:
    app = FastAPI(
        title="test_project_api",
        docs_url="/api/test_project_api",   # непонятно для чего эта ссылка? прочитать про swagger FastApi
        openapi_url="/api",                 # http://localhost:8844/api/test_project_api#/
        description="test_project_api",
        version="1.0.0",
    )

    # Маршруты
    app.include_router(
        admin_router, 
        prefix="/api/admin",
        tags=["admin"],
        dependencies=[Depends(admin_authenticate)],  # до передачи запроса в route должен выполнится любые нужная fun
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


if __name__ == "__main__":      # прочесть почему так? суровым языком.
    uvicorn.run("main:app", host="0.0.0.0", reload=False, port=app_config.APP_PORT)
