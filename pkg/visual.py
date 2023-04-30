from pyvis.network import Network


def _create_network(graph):
    network = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
    color_table = {
        'pdf': 'red',
        'url': 'blue',
    }

    table = {
        node.id: node
        for node in graph.all_nodes()
    }

    for node in table.values():
        kwargs = {}
        if hasattr(node, 'protocol'):
            kwargs['color'] = color_table[node.protocol]
        network.add_node(node.name, **kwargs)

    for node in table.values():
        for neighbor_id in node.links:
            neighbor = table[neighbor_id]
            network.add_edge(node.name, neighbor.name)

    return network


def generate_html(graph):
    network = _create_network(graph)
    return network.generate_html()
