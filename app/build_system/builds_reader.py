import yaml


class BuildsReader:
    @staticmethod
    def read_yaml_file(path: str) -> dict:
        with open(path, 'r') as stream:
            try:
                parsed_yaml: dict = yaml.safe_load(stream)
            except yaml.YAMLError as ex:
                print(ex)

        return parsed_yaml

    def read_builds(self, path: str) -> dict[str, list[str]]:
        parsed_yaml = self.read_yaml_file(path)

        builds = parsed_yaml['builds']
        builds_graph: dict[str, list[str]] = {}

        for build in builds:
            name, tasks = build['name'], build['tasks']
            builds_graph[name] = tasks

        return builds_graph

    def read_tasks(self, path: str) -> dict[str, list[str]]:
        parser_yaml = self.read_yaml_file(path)

        tasks = parser_yaml['tasks']
        tasks_graph: dict[str, list[str]] = {}

        for task in tasks:
            name, dependencies = task['name'], task['dependencies']
            tasks_graph[name] = dependencies

        return tasks_graph


build_reader = BuildsReader()
