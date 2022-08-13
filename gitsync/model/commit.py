from typing import Any


class Commit:
    def __init__(self, hash: str, title: str, author: str, parent_hashs: list[str]):
        self.hash = hash
        self.title = title
        self.author = author
        self.parent_hashs = parent_hashs

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        hashes = ",".join([f'"{hash}"' for hash in self.parent_hashs])
        return f'Commit(hash="{self.hash}", title="{self.title}", author="{self.author}", parent_hashs=[{hashes}])'
