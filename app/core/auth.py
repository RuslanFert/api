from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

from app.config.config import app_config
from app.const import FORBIDDEN_ERROR

X_ADMIN_API_SECRET = APIKeyHeader(
    name="X-ADMIN-API-SECRET", auto_error=False
)


async def admin_authenticate(
    x_api_secret: str = Depends(X_ADMIN_API_SECRET),
):
    """
    Проверка доступа к админским методам api.

    :param x_api_secret: Секретный ключ
    """
    if x_api_secret != app_config.ADMIN_API_SECRET:
        raise HTTPException(status_code=403, detail=FORBIDDEN_ERROR)
