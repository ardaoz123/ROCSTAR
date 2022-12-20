from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.user import router as user_router
from .routes.item import router as item_router
from .database import init_db

app = FastAPI()

app.include_router(user_router, tags=["user-router"], prefix="/user")
app.include_router(item_router, tags=["workflow-router"], prefix="/item")


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "server is running!"}
