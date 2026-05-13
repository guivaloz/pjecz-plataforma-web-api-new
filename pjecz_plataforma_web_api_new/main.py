"""
PJECZ Plataforma Web API new
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from fastapi_pagination import add_pagination
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded


def create_app() -> FastAPI:
    """Crea la aplicación FastAPI"""

    # FastAPI
    app = FastAPI(
        title="PJECZ Plataforma Web API new",
        description="API que proporciona datos para las consultas del sitio web.",
        docs_url="/docs",
        redoc_url=None,
    )

    # CORSMiddleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins.split(","),
        allow_credentials=False,
        allow_methods=["GET"],
        allow_headers=["*"],
    )

    # Mensaje de Bienvenida
    @app.get("/")
    async def root():
        """Mensaje de Bienvenida"""
        return {"message": "API que proporciona datos para las consultas del sitio web."}

    @app.get("/robots.txt", response_class=PlainTextResponse)
    async def robots():
        """robots.txt to disallow all agents"""
        return """User-agent: *\nDisallow: /"""

    # Entregar
    return app
