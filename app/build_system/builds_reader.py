from pathlib import Path

import yaml

from app.exceptions import BuildFileNotExists, IncorrectBuildFileException
from app.logger import logger


class BuildsReader:
    @staticmethod
    def read_yaml_file(path_to_file: str) -> dict:
        path = Path(path_to_file)

        if not path.is_file():
            raise BuildFileNotExists(path_to_file)

        with path.open(mode="r") as stream:
            try:
                parsed_yaml: dict = yaml.safe_load(stream)
            except yaml.YAMLError as ex:
                logger.exception(ex)
                raise IncorrectBuildFileException(path_to_file) from ex

        return parsed_yaml

    def read_builds(self, path: str) -> dict[str, list[str]]:
        parsed_yaml = self.read_yaml_file(path)

        try:
            builds = parsed_yaml["builds"]
            builds_graph: dict[str, list[str]] = {}

            for build in builds:
                name, tasks = build["name"], build["tasks"]
                builds_graph[name] = tasks
        except KeyError as ex:
            logger.exception(ex)
            raise IncorrectBuildFileException(path) from ex

        return builds_graph

    def read_tasks(self, path: str) -> dict[str, list[str]]:
        parser_yaml = self.read_yaml_file(path)

        try:
            tasks = parser_yaml["tasks"]
            tasks_graph: dict[str, list[str]] = {}

            for task in tasks:
                name, dependencies = task["name"], task["dependencies"]
                tasks_graph[name] = dependencies
        except KeyError as ex:
            logger.exception(ex)
            raise IncorrectBuildFileException(path) from ex

        return tasks_graph


reader = BuildsReader()
