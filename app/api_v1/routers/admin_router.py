from fastapi import APIRouter


admin_router = APIRouter()


@admin_router.get("/health")
async def health_check():
    return {"message": "API is working"}
