from __future__ import annotations
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Graph:
    def __init__(self):
        uri = "localhost:27017"
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client.pkg
        self.__graph = db.graph
        self.__cache = {}

    def __create_node(self, raw_node):
        node_id = raw_node['_id']
        if node_id not in self.__cache:
            node = Node(self, raw_node)
            self.__cache[node_id] = node
            return node
        else:
            return self.__cache[node_id]

    def find_one(self, **kwargs):
        raw_node = self.__graph.find_one(kwargs)
        if raw_node:
            return self.__create_node(raw_node)
        else:
            return None

    def find(self, **kwargs):
        return [self.__create_node(raw_node) for raw_node in self.__graph.find(kwargs)]

    def find_on_name(self, regex):
        return self.find(name={'$regex': regex, '$options': 'i'})

    def find_on_id(self, id):
        return self.find_one(_id=id)

    def all_nodes(self):
        return self.find()



class Node:
    def __init__(self, graph, raw_node):
        self.__graph = graph
        self.__raw_node = raw_node
        self.__children_cache = None

    @property
    def id(self):
        return self.__raw_node['_id']

    @property
    def children(self):
        if not self.__children_cache:
            self.__children_cache = [
                self.__graph.find_on_id(id)
                for id in self.__raw_node['links']
            ]
        return self.__children_cache

    def descendants(self, max_depth=None):
        max_depth = max_depth or float('inf')
        result = set()
        todo = [(self, 0)]
        while todo:
            next, depth = todo.pop()
            if depth <= max_depth and next not in result:
                result.add(next)
                for child in next.children:
                    todo.append((child, depth + 1))
        return result

    def __getattr__(self, attribute):
        if attribute in self.__raw_node:
            return self.__raw_node[attribute]
        else:
            raise AttributeError()

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.id == other.id
        else:
            return NotImplemented

    def fields(self):
        return self.__raw_node.items()
