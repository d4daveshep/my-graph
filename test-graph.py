import pytest

from graph import Graph
import pytest

from graph import Graph


@pytest.fixture()
def small_graph():
    graph = Graph()
    graph.add_relationship("Andrew", "is a", "Chief Engineer")
    graph.add_relationship("Andrew", "works on", "TWG")
    graph.add_relationship("TWG", "aka", "The Warehouse Group")
    return graph


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


def test_json_dump(small_graph):
    json_doc = small_graph.to_json()
    print(json_doc)
    pass
