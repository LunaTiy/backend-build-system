from fastapi import APIRouter

from app.build_system.builds import TasksBuilder
from app.build_system.schemas import SchemaRequestBuild

router = APIRouter(
    prefix="/build-system",
    tags=["Builds"]
)


@router.post("/get-tasks/")
async def get_tasks(build_request: SchemaRequestBuild) -> list[str]:
    """Resolve all tasks for build"""
    return TasksBuilder.get_tasks_for_build(build_request.build)
