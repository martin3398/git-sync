from typing import Optional

from elasticsearch import Elasticsearch


class ElasticConnection:
    def __init__(self, url: str, username: str, password: str, index: str, cert_location: Optional[str] = None):
        if cert_location:
            self.elastic = Elasticsearch(url, basic_auth=(username, password), ca_certs=cert_location)
        else:
            self.elastic = Elasticsearch(url, basic_auth=(username, password))
