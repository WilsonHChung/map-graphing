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
        self.nodes = set() #Note, using list instead of a set, since Nodes have 3 members, also given data is known to be set
        self.edges = defaultdict(set) #nodes are key, example-node 4:edges 4-5,4-6 node 5:5-4,4-6)
        self.nodeCordinates= defaultdict(list) #key=node, value = xcord,ycord list
        self.distances={}
        # 0:[3,4,5]
        # 1:[5,6,0]

    def add_node(self, node,xcord,ycord):
        #self.nodes.append(node)
        self.nodes.add(node)
        self.nodeCordinates[node].append(xcord )
        self.nodeCordinates[node].append(ycord)

    def add_edge(self, e):
        assert ( isinstance(e,Edge) )
        v=e.either()
        w=e.other(v)
        self.edges[v].add( w )
        self.edges[w].add( v )
        #ADDING DISTANCES
        self.distances[(w,v)]=e.weight
        self.distances[v,w] =e.weight
        #add distance to weight in future

#class Node:
   # def __init__(self, value,xcord,ycord):
        #self.val=value
       # self.xcord=xcord
       # self.ycord=ycord

class Edge:
    def __init__(self, node1,node2,graph):
       # assert (isinstance(node1, Node))
       # assert (isinstance(node2, Node))
        node1Cord=graph.nodeCordinates[node1]
        node2Cord=graph.nodeCordinates[node2]
        self.weight=distance(node1Cord[0],node2Cord[0],node1Cord[1],node2Cord[1])
        self.node1=node1
        self.node2=node2
        self.NodePair=[node1,node2]

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
    for myNode in range(10):

        xcord=random.randint(1,20)
        ycord=random.randint(1,20)
        #myNode=Node(i,xcord,ycord)
        graph.add_node(myNode,xcord,ycord)
        #graph.add_node(Node(i,xcord,ycord))
        print("adding Node",myNode, "X cord ",xcord ,"Y cord ", ycord)
    #creating like 10 random edges
    for i in range(10):
        a=random.randint(1,9) #some random node value
        b=random.randint(1,9)
        c= random.randint(1,9)
        myEdge=Edge(a,b,graph)
        myEdge1 = Edge(a, c,graph)
        graph.add_edge( myEdge )
        graph.add_edge(myEdge1)
        print("adding Edge",a,"-",b," weight-",myEdge.weight )

    for x in sorted(graph.edges):
        print(x,graph.edges[x])
    #sort hash table
#



