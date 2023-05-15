from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .api import api_router
from .db.session import db_engine

app = FastAPI(title='Miller Challenge')

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event('startup')
async def init_db() -> None:
    await db_engine.create_all()


app.include_router(api_router)
