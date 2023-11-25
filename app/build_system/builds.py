from app.build_system.builds_reader import reader


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
