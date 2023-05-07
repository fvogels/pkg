from pyvis.network import Network
from functools import reduce


def _create_network(graph, names, depth):
    network = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
    color_table = {
        'pdf': 'red',
        'url': 'blue',
    }

    table = {
        node.id: node
        for node in graph.all_nodes()
    }

    node_sets = [
        {
            selected
            for node in graph.find_on_name(name)
            for selected in node.descendants(max_depth=depth)
        }
        for name in names
    ]
    selected_nodes = reduce(lambda x, y: x & y, node_sets)

    for node in selected_nodes:
        kwargs = {}
        if hasattr(node, 'protocol'):
            kwargs['color'] = color_table[node.protocol]
        network.add_node(node.name, **kwargs)

    for node in selected_nodes:
        for neighbor_id in node.links:
            neighbor = table[neighbor_id]
            if neighbor in selected_nodes:
                network.add_edge(node.name, neighbor.name)

    return network


def generate_html(graph, names, depth):
    network = _create_network(graph, names, depth)
    return network.generate_html()
