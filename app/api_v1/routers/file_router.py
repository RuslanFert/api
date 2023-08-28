from typing import Annotated
from fastapi import APIRouter
from fastapi import File, UploadFile

router_file = APIRouter()


@router_file.post("/files")
async def create_files(file: Annotated[bytes, File()]):
    return {"200" + " файл создан " + "file_size": len(file)}


@router_file.post("/uploadfile")
async def create_unload_file(file: UploadFile):
    return {"200" + " файл создан " + "filename": file.filename}


@router_file.delete("/")
async def del_file():
    return {"200" + " файл успешно удален "}
