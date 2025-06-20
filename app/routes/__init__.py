from fastapi import APIRouter
from .restaurant_routes import router as restaurant_router
from .order_routes import router as order_router
from .auth_routes import router as auth_router

router = APIRouter()
router.include_router(restaurant_router)
router.include_router(order_router)
router.include_router(auth_router)