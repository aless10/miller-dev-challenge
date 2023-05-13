from fastapi import FastAPI

from .api import api_router
from .db.session import db_engine

app = FastAPI(title='Miller Challenge')


@app.on_event('startup')
async def init_db() -> None:
    await db_engine.create_all()


app.include_router(api_router)
