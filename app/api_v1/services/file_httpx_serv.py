import httpx
import json
import logging
# import base64
from httpx import ConnectError
from starlette.responses import JSONResponse
from app.models.httpx_model import RequestBodyModel


async def post_page(body: RequestBodyModel):
    async with httpx.AsyncClient() as client:
        try:
            reqs = await client.get(body.url)
        except ConnectError as e:
            logging.error(e)
            return JSONResponse(status_code=404, content=f"ошибка ConnectError: {e}")
        else:
            raw_data = reqs.content
            # raw_data_b64 = base64.b64encode(raw_data)
            # data_byte = base64.b64decode(raw_data_b64)
            data_str = raw_data.decode(reqs.encoding)
            data = json.dumps(data_str, indent=4, sort_keys=True)   # убрал переменную content
            # сделал форматирование - сразу в строку JSON
            return JSONResponse(status_code=reqs.status_code, content=data)
        finally:
            print("метод get_connect отработал корректно")
