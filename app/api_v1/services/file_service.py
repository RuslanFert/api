from httpx import HTTPError
from pydantic import BaseModel
import os


class WorkWithFile(BaseModel):

    @staticmethod
    async def get_file(file_name: str):
        """Открывает указанный файл для чтения"""
        file_path = f".\\{file_name}"
        try:
            with open(file_path, "r") as file:
                file.read()
        except FileNotFoundError as e:
            raise HTTPError(message=f"файл не найден, ошибка {e}")
        return True

    @staticmethod
    async def create_file(file_name: str, message: str | None = None):
        """Создает файл, присваивает ему имя, при необходимости записывает данные в файл"""
        file_path = f".\\{file_name}"
        try:
            with open(file_path, "w") as file:
                file.write(message)
        except Exception as e:
            raise HTTPError(message=f"файл не создан, ошибка {e}")
        return True

    @staticmethod
    async def add_info_file(file_name: str, new_info: str):
        """Если файл существует - изменяет тело файла - записывает новые данные"""
        file_path = f".\\{file_name}"
        try:
            with open(file_path, "w") as file:
                file.write(new_info)
        except Exception as e:
            raise HTTPError(message=f"файл не найден, ошибка {e}")
        return True

    @staticmethod
    async def del_file(file_name: str):
        """Удаляет выбранный файл при его наличии"""
        file_path = f".\\{file_name}"
        try:
            os.remove(file_path)
        except Exception as e:
            raise HTTPError(message=f"файл не найден, ошибка {e}")
        return True
