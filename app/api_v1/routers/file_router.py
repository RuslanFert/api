from fastapi import APIRouter
from httpx import HTTPError
from starlette.responses import JSONResponse

from app.api_v1.services.file_service import WorkWithFile
from app.models.file_model import FileTestRequestModel, FileUpdateRequestModel

file_router = APIRouter()


@file_router.get("/files")
async def get_file(file_name: str):
    result = await WorkWithFile.get_file(file_name=file_name)
    if result:
        return JSONResponse(status_code=200, content=f"Файл прочитан")


@file_router.post("/files")
async def create_file(body: FileTestRequestModel):
    result = await WorkWithFile.create_file(file_name=body.file_name, message=body.message)
    if result:
        return JSONResponse(status_code=200, content=f"Файл создан")


@file_router.put("/files")
async def upload_file(body: FileUpdateRequestModel):
    result = await WorkWithFile.add_info_file(file_name=body.file_name, new_info=body.new_info)
    if result:
        return JSONResponse(status_code=200, content="Файл обновлен")


@file_router.delete("/files")
async def del_file(file_name: str | None = None):
    if not file_name:
        raise HTTPError(message=f"не указано имя удаляемого файла")
    await WorkWithFile.del_file(file_name=file_name)
    return JSONResponse(status_code=200, content="Файл удален")
