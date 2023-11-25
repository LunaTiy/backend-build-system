from fastapi import APIRouter

from app.build_system.schemas import SchemaRequestBuild

router = APIRouter(
    prefix="/build-system",
    tags=["Builds"]
)


@router.post("/get-tasks/")
async def get_tasks(build_request: SchemaRequestBuild) -> list[str]:
    return []
