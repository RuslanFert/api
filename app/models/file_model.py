from pydantic import BaseModel, Field


class FileTestRequestModel(BaseModel):
    file_name: str = Field(default=None)
    message: str = Field(default=None)


class FileUpdateRequestModel(BaseModel):
    file_name: str = Field(default=None)
    new_info: str = Field(default=None)
