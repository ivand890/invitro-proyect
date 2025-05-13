from fastapi import APIRouter
from .review import review_router

router_v1 = APIRouter(prefix="/v1", tags=["v1"])
router_v1.include_router(review_router)
