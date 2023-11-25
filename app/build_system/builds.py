from app.build_system.builds_reader import reader
from app.exceptions import TasksKeyError


class TasksBuilder:
    tasks: dict[str, list[str]]
    builds: dict[str, list[str]]

    @classmethod
    def init_tasks_and_build(
            cls,
            path_to_tasks_yaml: str,
            path_to_builds_yaml: str
    ) -> None:
        cls.tasks = reader.read_tasks(path_to_tasks_yaml)
        cls.builds = reader.read_builds(path_to_builds_yaml)

    @classmethod
    def get_tasks_for_build(cls, build: str) -> list[str]:
        tasks_for_build = cls.builds[build]
        result_tasks: list[str] = []

        for task in tasks_for_build:
            result_tasks += cls.resolve_task(task)

        return result_tasks

    @classmethod
    def resolve_task(cls, task: str) -> list[str]:
        if task not in cls.tasks:
            raise TasksKeyError(task)

        dependencies = cls.tasks[task]
        resolved: list[str] = []

        for dependent_task in dependencies:
            resolved += cls.resolve_task(dependent_task)

        resolved.append(task)
        return resolved
