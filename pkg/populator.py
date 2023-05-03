from __future__ import annotations
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime


class GraphPopulator:
    def __init__(self):
        uri = "localhost:27017"
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client.pkg
        self.__graph = db.graph

    def add_node(self, *, name, **fields) -> NodeId:
        graph = self.__graph
        if node := graph.find_one({'name': name}):
            return NodeId(self, node['_id'])
        else:
            fields = {
                'date': datetime.utcnow(),
                'name': name,
                'links': [],
                **fields
            }
            return NodeId(self, graph.insert_one(fields).inserted_id)

    def find_node_with_name(self, name):
        return self.__graph.find_one({'name': name})

    def add_url(self, *, name, url, **kwargs):
        return self.add_node(
            name=name,
            url=url,
            protocol='url',
            **kwargs,
        )

    def add_pdf(self, *, name, filename, **kwargs):
        return self.add_node(
            name=name,
            protocol='pdf',
            filename=filename,
            **kwargs,
        )

    def link(self, from_node, to_node):
        filter = {'_id': from_node}
        update = { '$addToSet': { 'links': to_node } }
        self.__graph.update_one(filter, update)


class NodeId:
    def __init__(self, graph, id):
        self.__graph = graph
        self.__id = id

    @property
    def id(self):
        return self.__id

    def link(self, *nodes: NodeId):
        for node in nodes:
            self.__graph.link(node.id, self.id)
        return self
