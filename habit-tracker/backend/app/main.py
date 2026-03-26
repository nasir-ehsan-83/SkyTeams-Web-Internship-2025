from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.database import init_db
from app.routers import user

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user.router)