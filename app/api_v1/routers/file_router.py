from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.api_v1.services.file_service import WorkWithFile


router_file = APIRouter()


@router_file.post("/files")
async def create_files():
    await WorkWithFile.create_file()
    return JSONResponse(status_code=200, content="Файл создан")


@router_file.post("/uploadfile")
async def unload_file():
    await WorkWithFile.add_info_file(file_name=None)
    return JSONResponse(status_code=200, content="Файл обновлен")


@router_file.delete("/")
async def del_file():
    await WorkWithFile.del_file(file_name=None)
    return JSONResponse(status_code=200, content="Файл удален")
