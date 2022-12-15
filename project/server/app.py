from fastapi import FastAPI
from .routes.user import router as user_router
from .routes.workflow import router as workflow_router
from .database import init_db

app = FastAPI()

app.include_router(user_router, tags=["user-router"], prefix="/user")
app.include_router(workflow_router, tags=["workflow-router"], prefix="/workflow")


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello, World!"}
