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
        raw_node = self.__graph.find_one(kwargs)
        if raw_node:
            return Node(raw_node)
        else:
            return None

    def find(self, **kwargs):
        return map(Node, self.__graph.find(kwargs))

    def all_nodes(self):
        return self.find()



class Node:
    def __init__(self, raw_node):
        self.__raw_node = raw_node

    @property
    def id(self):
        return self.__raw_node['_id']

    def __getattr__(self, attribute):
        if attribute in self.__raw_node:
            return self.__raw_node[attribute]
        else:
            raise AttributeError()
