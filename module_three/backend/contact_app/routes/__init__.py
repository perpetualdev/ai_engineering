from fastapi import APIRouter
from .delete import router as delete_router
from .get import router as get_router
from .post import router as post_router
from .put import router as put_router
from .patch import router as patch_router

api_router = APIRouter()
api_router.include_router(delete_router)
api_router.include_router(get_router)
api_router.include_router(post_router)
api_router.include_router(put_router)
api_router.include_router(put_router)
api_router.include_router(patch_router)
