from datetime import datetime, timedelta
from typing import Optional

from gitlab import Gitlab

from gitsync.handler.repo_handler import RepoHandler
from gitsync.model.commit import Commit
from gitsync.model.project import Project


# TODO: add error handling (e.g., 401)
class GitlabHandler(RepoHandler):
    def __init__(self, url: str, config: Optional[dict] = None):
        super().__init__(url, config)

        token = config.get("token", None) if config else None

        self.gitlab = Gitlab(url, private_token=token)
        self.gitlab.auth()

    def get_projects(self) -> list[Project]:
        return [
            Project(project.id, project.name)
            for project in self.gitlab.projects.list(iterator=True, membership=True, all=True)
        ]

    def get_commits(self, project: Project, since: Optional[datetime] = None) -> dict[str, Commit]:
        return {
            commit.id: Commit(commit.id, commit.title, commit.author_name, commit.parent_ids)
            for commit in self.gitlab.projects.get(project.id).commits.list(all=True, since=since)
        }
