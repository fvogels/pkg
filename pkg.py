import click
from functools import reduce
from pkg.graph import Graph
from pkg.visual import generate_html
from pkg.protocols import apply_protocol
from bson import ObjectId
from rich.console import Console
from rich.table import Table
import webbrowser
import tempfile


@click.group()
def cli():
    pass


@cli.command()
@click.argument('id')
def fetch(id):
    graph = Graph()
    object_id = ObjectId(id)
    node = graph.find_one(_id=object_id)
    apply_protocol(node)


@cli.command()
@click.argument('names', nargs=-1)
@click.option('--format', type=click.Choice(['full', 'table'], case_sensitive=False), default='full')
def find(names, format):
    graph = Graph()
    nodesets = [
        {
            descendant
            for node in graph.find_on_name(name)
            for descendant in node.descendants()
        }
        for name in names
    ]
    intersection = reduce(lambda x, y: x & y, nodesets)

    console = Console()
    match format:
        case 'full':
            for node in intersection:
                table = Table(show_header=False)
                table.add_column('Key', style='bold')
                table.add_column('Value')
                for key, value in node.fields():
                    table.add_row(key, str(value))
                console.print(table)
        case 'table':
            table = Table(show_header=False, show_edge=False, show_lines=False)
            table.add_column('Name', style='bold')
            table.add_column('Id')
            for node in intersection:
                table.add_row(str(node.id), node.name)
            console.print(table)


@cli.command()
@click.argument('names', nargs=-1)
@click.option('--depth', default=1)
def graph(names, depth):
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as file:
        graph = Graph()
        html = generate_html(graph, names, depth)
        print(html, file=file)
    webbrowser.open(file.name)


@cli.command()
def verify():
    graph = Graph()
    nodes = graph.all_nodes()
    for node in nodes:
        for child in node.children:
            for grandchild in child.children:
                if grandchild in node.children:
                    print(f'{node.name} -> {child.name} -> {grandchild.name}')


if __name__ == '__main__':
    cli()
