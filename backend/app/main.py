from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.api.middleware import register_middleware
from app.api.router import api_router
from app.core.config import get_settings
from app.core.exceptions import register_exception_handlers
from app.core.lifespan import lifespan

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise AI-Native Low-Code API Orchestration Platform",
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)

register_middleware(app)

register_exception_handlers(app)

app.include_router(api_router)