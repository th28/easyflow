import numpy as np


class DirectedGraph:
    """Simple data structure to model a directed graph"""

    def __init__(self, nodes={}, edges={}):
        self.nodes = nodes
        self.edges = edges

    def __str__(self):
        return str(self.edges)

    def add_node(self, name, value):
        self.nodes[name] = value

    def add_edge(self, start, end, capacity, cost):
        self.edges[(start, end)] = [capacity, cost]
