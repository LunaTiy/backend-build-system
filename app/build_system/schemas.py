from typing import Annotated
from fastapi import Body
from pydantic import BaseModel, field_validator

from app.build_system.builds import TasksBuilder
from app.logger import logger


class SchemaRequestBuild(BaseModel):
    build: Annotated[str, Body(description="Build name")]

    @field_validator("build")  # noqa
    @classmethod
    def validate_build(cls, value: str) -> str:
        if value not in TasksBuilder.builds:
            raise ValueError(f"That build <<{value}>> does not exists in possible builds")

        return value
