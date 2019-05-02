import Dheap
import sys
import unittest

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict() #using adj list, nodes are a key for edges

    def add_node(self, node):
        #Adding the Node Object
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = Edge(to_node, length)
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

#TODO implement these functions
#Def Idea 1PQ():
#Def A*? We might need a completely different function for this
#Def Idea 3 PQ():

class Edge:
    def __init__(self, node1,node2 ):
        #we can take this part out afterwards
        #if not isinstance(node1,Node) or not isinstance(node2,Node):
           # raise ValueError("Node not passed")
        weight=distance(node1.xcord,node1.ycord,node2.xcord,node2.ycord)
        self.node1=node1
        self.node2=node2

#def Idea1Dij():


