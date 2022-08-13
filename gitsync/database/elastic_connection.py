from typing import Optional, Iterable

from elasticsearch import Elasticsearch

from gitsync.model.commit import Commit
from gitsync.model.project import Project


class ElasticConnection:
    def __init__(self, url: str, username: str, password: str, index: str, cert_location: Optional[str] = None):
        if cert_location:
            self.elastic = Elasticsearch(url, basic_auth=(username, password), ca_certs=cert_location)
        else:
            self.elastic = Elasticsearch(url, basic_auth=(username, password))

        self.index = index

    def add_commit(self, commit: Commit, project: Project):
        commit_dict = {
            **commit.__dict__,
            "project": project.full_name,
        }

        self.elastic.index(index=self.index, document=commit_dict, id=commit.hash)

    def add_commits(self, commits: Iterable[Commit], project: Project):
        for commit in commits:
            self.add_commit(commit, project)
