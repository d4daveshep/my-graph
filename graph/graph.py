from graph.node import Node


class Graph:
    def __init__(self):
        self.relationships = []
        self.nodes = {}

    def add_relationship(self, subject_node: str, relationship: str, object_node: str) -> None:
        pass

    def add_node(self, name:str):
        if name not in self.nodes:
            self.nodes[name] = Node(name)


