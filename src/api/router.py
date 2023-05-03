from fastapi import APIRouter
import src.api.user.view as user
import src.api.product.view as product

api_router = APIRouter()

api_router.include_router(user.router, prefix="/pessoas", tags=["pessoas"])

api_router.include_router(product.router, prefix="/pessoas", tags=["pessoas"])
