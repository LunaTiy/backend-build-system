from contextlib import AbstractAsyncContextManager, asynccontextmanager

from fastapi import FastAPI

from app.build_system.builds import TasksBuilder
from app.build_system.router import router as build_system_router
from app.constants import PATH_TO_BUILDS, PATH_TO_TASKS


@asynccontextmanager
async def lifespan(
        fastapi_app: FastAPI  # noqa: ARG001
) -> AbstractAsyncContextManager[None]:
    TasksBuilder.init_tasks_and_build(PATH_TO_TASKS, PATH_TO_BUILDS)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(build_system_router)
