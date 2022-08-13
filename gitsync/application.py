import logging

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

        self.logger = None
        self.init_logger()

    def init_logger(self):
        logging.basicConfig()

        self.logger = logging.getLogger("gitsync")
        self.logger.setLevel(self.config.get("loglevel", logging.WARNING))

    def run(self) -> None:
        for source in self.config["sources"]:
            class_name = handlers[source["type"]]
            handler = class_name(source.get("url", None), source.get("config", None))

            projects = handler.get_projects()
            for project in projects:
                self.elastic.add_commits(handler.get_commits(project).values(), project)
                self.logger.info(f"Synced project '{project.full_name}'")
