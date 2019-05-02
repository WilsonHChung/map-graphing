import Dheap
import sys
import unittest
from collections import defaultdict
import random

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

class Graph:
    def __init__(self):
        self.nodes = list() #Note, using list instead of a set, since Nodes have 3 members, also given data is known to be set
        self.edges = dict() #nodes are key, example-node 4:edges 4-5,4-6 node 5:5-4,4-6)

    def add_node(self, node):
        assert ( isinstance(node,Node) )
        #self.nodes.add(node)
        self.nodes.append(node)

    def add_edge(self, e):
        assert ( isinstance(e,Edge) )
        v=e.either()
        w=e.other(v)
        self.edges[v]=e
        self.edges[w]=e
        #node object is the key, not node value
class Node:
    def __init__(self, value,xcord,ycord):
        self.val=value
        self.xcord=xcord
        self.ycord=ycord

class Edge:
    def __init__(self, node1,node2 ):
        assert (isinstance(node1, Node))
        assert (isinstance(node2, Node))
        self.weight=distance(node1.xcord,node1.ycord,node2.xcord,node2.ycord)
        self.node1=node1
        self.node2=node2
        
    def either(self):
        return self.node1

    def other(self,vertex):
        if vertex == self.node1 :
            return self.node2
        else:
            return self.node1

    def compareTo(self,that ):
        assert( isinstance(that,Edge))
        if self.weight < that.weight():
            return -1
        elif self.weight > that.weight :
            return 1
        else:
            return 0


if __name__ == '__main__':
    graph = Graph()
    #adding nodes
    for i in range(10):
        xcord=random.randint(1,20)
        ycord=random.randint(1,20)
        myNode=Node(i,xcord,ycord)
        graph.add_node(myNode)
        #graph.add_node(Node(i,xcord,ycord))
        print("adding Node",i, "X cord ",xcord ,"Y cord ", ycord)
    #creating like 10 random edges
    for i in range(10):
        a=graph.nodes[random.randint(1,10)]
        b=graph.nodes[random.randint(1,10)]
        myEdge=Edge(a,b)
        graph.add_edge( myEdge )
        print("adding Edge",a.val,"-",b.val," weight-",myEdge.weight )
    for x,y in graph.edges:
        print(x,y)


