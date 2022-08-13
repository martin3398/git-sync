class Project:
    def __init__(self, id: int, name: str, full_name: str):
        self.id = id
        self.name = name
        self.full_name = full_name

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f'Project(id={self.id}, name="{self.name}, full_name="{self.full_name}")'
