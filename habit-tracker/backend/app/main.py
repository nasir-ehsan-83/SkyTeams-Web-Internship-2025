from fastapi import FastAPI

from app.db.database import init_db
from app.routers import user
from fastapi_offline_docs.offline_docs import setup_offline_docs

"""@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
"""
app = FastAPI()
setup_offline_docs(app)

@app.on_event("startup")
async def get_db():
    await init_db()
    yield


app.include_router(user.router)