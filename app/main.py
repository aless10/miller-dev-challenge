from fastapi import FastAPI

from .api import api_router

app = FastAPI(title='Miller Challenge')

# asyncio.get_event_loop().create_task(db_engine.create_all())

app.include_router(api_router)
