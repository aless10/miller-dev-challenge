from fastapi import FastAPI

from .api import api_router

app = FastAPI(title='Miller Challenge')

app.include_router(api_router)
