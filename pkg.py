import click
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
@click.option('--name')
def find(name):
    graph = Graph()
    kwargs = {}
    if name:
        kwargs['name'] = { '$regex': name, '$options': 'i' }
    nodes = graph.find(**kwargs)
    console = Console()
    for node in nodes:
        table = Table(show_header=False)
        table.add_column('Key', style='bold')
        table.add_column('Value')
        for key, value in node.items():
            table.add_row(key, str(value))
        console.print(table)


@cli.command()
def graph():
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as file:
        graph = Graph()
        html = generate_html(graph)
        print(html, file=file)
    webbrowser.open(file.name)


if __name__ == '__main__':
    cli()
