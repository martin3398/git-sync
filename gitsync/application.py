import yaml


class Application:
    def __init__(self) -> None:
        try:
            with open("config.yml", "r") as file:
                self.config = yaml.load(file)
        except FileNotFoundError:
            pass


def run(self) -> None:
    pass
