import pytest

from graph.graph import Graph


def test_create_relationship():
    graph = Graph()
    graph.add_relationship("Andrew", "is a", "Chief Engineer")
    graph.add_relationship("Andrew", "works on", "TWG")
    graph.add_relationship("TWG", "aka", "The Warehouse Group")
    
    assert len(graph.relationships) == 3
