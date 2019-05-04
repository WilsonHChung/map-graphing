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

class EdgeWeightedDiGraph:
    NumberOfNodes=0
    NumberOfEdges=0
    nodes = set()  # Note, using list instead of a set, since Nodes have 3 members, also given data is known to be set
    edges = defaultdict(set)  # nodes are key, example-node 4:edges 4-5,4-6 node 5:5-4,4-6)
    nodeCordinates = defaultdict(list)  # key=node, value = xcord,ycord list
    distances = {}

    def add_edge(self, e):
        assert (isinstance(e, DirectedEdge))
        node1=e.node1
        node2=e.node2
        self.edges[node1].add(node2)
        self.distances[node1, node2] = e.weight

    def add_node(self, node,xcord,ycord):
        #self.nodes.append(node)
        self.nodes.add(node)
        self.nodeCordinates[node].append(xcord)
        self.nodeCordinates[node].append(ycord)

    def compareTo(self,that ):
        assert( isinstance(that,DirectedEdge))
        if self.weight < that.weight():
            return -1
        elif self.weight > that.weight :
            return 1
        else:
            return 0

#SAME THING BUT THE ONLY MOD THE WEIGHT
class DirectedEdge:
    def __init__(self, node1, node2,graph):
        self.node1 = node1
        self.node2 = node2
        node1Cord = graph.nodeCordinates[node1]
        node2Cord = graph.nodeCordinates[node2]

        self.weight = distance(node1Cord[0], node2Cord[0], node1Cord[1], node2Cord[1])

    def returnWeight(self):
        return self.weight

    def fromVertex(self):
        return self.node1

    def toVertex(self):
        return self.node2

if __name__ == '__main__':
    #UNIT TEST, have a seperate main function to test input 6 or something
    graph = EdgeWeightedDiGraph()
    NumberOfNodes=5
    NumberOfEdges=9
    xcord= random.sample(range(1, 100*NumberOfNodes), NumberOfNodes)
    ycord= random.sample(range(1, 100*NumberOfNodes), NumberOfNodes)

    for i in range(NumberOfNodes):
        graph.add_node(i,xcord[i],ycord[i])
        #graph.add_node(Node(i,xcord,ycord))
        print("adding Node",i, "X cord ",xcord[i] ,"Y cord ", ycord[i] )
    for i in range(NumberOfEdges):
        firstNode=random.randint(0,NumberOfNodes-1)
        secondNode = random.randint(0,NumberOfNodes-1)

        while(firstNode==secondNode):
            secondNode = random.randint(0, NumberOfNodes-1)

        myEdge= DirectedEdge(firstNode,secondNode,graph)
        print("adding Edge",firstNode, "- ",secondNode, "Distance", myEdge.weight)
        graph.add_edge(myEdge)


    for x in graph.edges:
        print(x,graph.edges[x])





#