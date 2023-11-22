from fastapi import APIRouter, Request
from starlette.responses import JSONResponse

from app.models.httpx_model import RequestBodyModel
from app.api_v1.services.file_httpx_serv import post_page

httpx_router = APIRouter()


@httpx_router.post("/get_connect")
async def get_connect(request: Request, body: RequestBodyModel):
    result = await post_page(body=body, request=request)
    return result
