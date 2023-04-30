from __future__ import annotations
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Graph:
    def __init__(self):
        uri = "localhost:27017"
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client.pkg
        self.__graph = db.graph

    def find_one(self, **kwargs):
        return self.__graph.find_one(kwargs)

    def find(self, **kwargs):
        return self.__graph.find(kwargs)


class NodeId:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id
