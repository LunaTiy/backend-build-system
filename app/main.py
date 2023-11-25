from contextlib import asynccontextmanager, AbstractAsyncContextManager

from fastapi import FastAPI

from app.build_system.builds import TasksBuilder
from app.build_system.router import router as build_system_router


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI) -> AbstractAsyncContextManager[None]:
    TasksBuilder.init_tasks_and_build("builds/tasks.yaml", "builds/builds.yaml")
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(build_system_router)
