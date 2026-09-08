from fastapi import FastAPI
from controller.api import router

app = FastAPI(
    title="API de Filmes",
    version="1.0.0"
)

app.include_router(router)