from node import Node


class Graph:
    def __init__(self):
        self.relationships = []
        self.nodes = {}

    def add_relationship(self, subject_name: str, relationship_name: str, target_name: str) -> None:
        subject = self.add_node(subject_name)
        target = self.add_node(target_name)
        subject.connections[relationship_name] = target_name

    def add_node(self, name:str) -> Node:
        if name not in self.nodes:
            node = Node(name)
            self.nodes[name] = node
            return node
        else:
            return self.nodes[name]



