class Node:
    def __init__(self, name:str):
        self.name = name
        self.connections = {}

    def to_json(self) -> str:
        return '{"name":"' + self.name + '"}'


