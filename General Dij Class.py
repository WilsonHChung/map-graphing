import Dheap
import sys
import unittest
from collections import defaultdict
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict() #nodes are key, example-node 4:edges 4-5,4-6 node 5:5-4,4-6)

    def add_node(self, node):
        #Adding the Node Object
        self.nodes.add(node)

    def add_edge(self, from_node, to_node):
        edge = Edge(to_node)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]
        from_node_edges[to_node.label] = edge

class Node:
    def __init__(self, value,xcord,ycord):
        self.val=value
        self.xcord=xcord
        self.ycord=ycord

class Edge:
    def __init__(self, node1,node2 ):
        #we can take this part out afterwards
        #if not isinstance(node1,Node) or not isinstance(node2,Node):
           # raise ValueError("Node not passed")
        self.weight=distance(node1.xcord,node1.ycord,node2.xcord,node2.ycord)
        self.node1=node1
        self.node2=node2



