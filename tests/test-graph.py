import pytest

from graph.graph import Graph
from graph.node import Node


def test_create_nodes():
    graph = Graph()
    graph.add_node("Andrew")

    assert "Andrew" in graph.nodes
    assert len(graph.nodes["Andrew"].connections) == 0

def test_create_relationship():
    graph = Graph()
    graph.add_relationship("Andrew", "is a", "Chief Engineer")
    graph.add_relationship("Andrew", "works on", "TWG")
    graph.add_relationship("TWG", "aka", "The Warehouse Group")
    
    assert len(graph.nodes) == 4
    assert len(graph.nodes["Andrew"].connections) == 2
    assert "is a" in graph.nodes["Andrew"].connections
    assert "Chief Engineer" in graph.nodes
