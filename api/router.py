from fastapi import APIRouter

from api.routes.model import router as model_router

router = APIRouter()


router.include_router(model_router, prefix="/model")
