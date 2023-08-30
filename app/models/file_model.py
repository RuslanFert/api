from pydantic import BaseModel, Field


class FileTestRequestModel(BaseModel):
    message: str = Field(default=None)
    file_name: str = Field(default=None)
