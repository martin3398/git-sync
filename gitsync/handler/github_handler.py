from datetime import datetime
from typing import Optional

from github import Github

from gitsync.handler.repo_handler import RepoHandler
from gitsync.model.commit import Commit
from gitsync.model.project import Project


# TODO: make implementation more efficient (if possible)
class GithubHandler(RepoHandler):
    def __init__(self, url: Optional[str], config: Optional[dict] = None):
        super().__init__(url, config)

        self.github = Github(config["token"])
        self.excluded = config.get("exclude", [])
        self.excluded_orgs = config.get("exclude_orgs", [])

        # TODO: implement project buffer logic
        self.project_buffer = {}

    def get_projects(self) -> list[Project]:
        projects = []
        for repo in self.github.get_user().get_repos():
            if repo.full_name in self.excluded:
                continue

            organization = repo.organization
            if organization and organization.login in self.excluded_orgs:
                continue

            projects.append(Project(repo.id, repo.full_name, f"github/{repo.full_name}"))

        return projects

    def get_commits(self, project: Project, since: Optional[datetime] = None) -> dict[str, Commit]:
        # TODO: implement 'since' logic
        return {
            commit.sha: Commit(
                commit.sha,
                commit.commit.message,
                commit.committer.name,
                [parent.sha for parent in commit.commit.parents],
            )
            for commit in self.github.get_repo(project.name).get_commits()
        }
