import pytest

from graph.graph import Graph
from graph.node import Node


def test_create_nodes():
    graph = Graph()
    graph.add_node("Andrew")

    assert "Andrew" in graph.nodes
    # assert len(andrew.connections) == 0

def test_create_relationship():
    graph = Graph()
    graph.add_relationship("Andrew", "is a", "Chief Engineer")
    graph.add_relationship("Andrew", "works on", "TWG")
    graph.add_relationship("TWG", "aka", "The Warehouse Group")
    
    assert len(graph.relationships) == 3
