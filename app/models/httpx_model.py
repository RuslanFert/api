from pydantic import BaseModel, Field


class RequestBodyModel(BaseModel):
    url: str = Field(default=None)
