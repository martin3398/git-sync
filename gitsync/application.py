import yaml
from yaml import FullLoader

from gitsync import config
from gitsync.database.elastic_connection import ElasticConnection
from gitsync.handler import handlers


class Application:
    def __init__(self) -> None:
        try:
            with open(config.config_file, "r") as file:
                self.config: dict = yaml.load(file, FullLoader)
        except FileNotFoundError:
            self.config: dict = config.default_config

        config.validate(self.config)

        self.elastic = ElasticConnection(**self.config["elastic"])

    def run(self) -> None:
        for source in self.config["sources"]:
            print(source)
            class_name = handlers[source["type"]]
            handler = class_name(source["url"], source.get("config", None))

            projects = handler.get_projects()
            print(projects)
            for project in projects:
                print(handler.get_commits(project))
