from fastapi import FastAPI
from contextlib import asynccontextmanager
from logging import info

from configs.loggin_config import setup_logging , logging_config
from configs.settings import settings


@asynccontextmanager
async def life_span(app : FastAPI):
    setup_logging()
    info("loggs setup")
    
    yield

app = FastAPI(
    title="Neburos backend",
    description="Api do sistema neburos, um sistema de gerenciamento financeiro open source e gratuito",
    version="0.1.0",
    lifespan=life_span,
    debug=settings.DEBUG
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_config=logging_config,reload=settings.DEBUG)
