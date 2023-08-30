from pydantic import BaseModel
import os

# создать класс, внутри асинхронные функции создать файл и удалить файл
# дальше импортировать его в файл роута


class WorkWithFile(BaseModel):
    @staticmethod
    async def create_file(file_name="file.txt", file_body=None):
        """Создает файл, присваивает ему имя, при необходимости записывает данные в файл"""
        new_file = open(input(file_name), "w+")
        new_file.write(file_body)
        new_file.close()

    @staticmethod
    async def add_info_file(file_name, file_body=None):
        """Если файл существует - изменяет тело файла - записывает новые данные"""
        os.path.isfile("/путь/к/файлу/file_name")
        new_file = open(input(file_name), "a+")
        new_file.write(file_body)
        new_file.close()

    @staticmethod
    async def del_file(file_name):
        """Удаляет выбранный файл при его наличии"""
        os.path.isfile("/путь/к/файлу/file_name")
        os.remove(file_name)
