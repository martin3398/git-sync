from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from gitsync.model.commit import Commit
from gitsync.model.project import Project


class RepoHandler(ABC):
    def __init__(self, url: Optional[str], config: Optional[dict] = None):
        pass

    @abstractmethod
    def get_projects(self) -> list[Project]:
        pass

    @abstractmethod
    def get_commits(self, project: Project, since: Optional[datetime] = None) -> dict[str, Commit]:
        pass
