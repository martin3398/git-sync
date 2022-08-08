from typing import Type

from gitsync.handler.github_handler import GithubHandler
from gitsync.handler.gitlab_handler import GitlabHandler
from gitsync.handler.repo_handler import RepoHandler
from gitsync.handler.ssh_handler import SshHandler

handlers: dict[str, Type[RepoHandler]] = {
    "github": GithubHandler,
    "gitlab": GitlabHandler,
    "ssh": SshHandler,
}
