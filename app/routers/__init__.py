from fastapi import APIRouter
from .v1 import router_v1

router = APIRouter()
router.include_router(router_v1)