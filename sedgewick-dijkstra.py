import math
from collections import defaultdict
from General_Dij_Class import IndexMinPQ, Graph

class EdgeWeightedDiagraph:
    def __init__(self, V):
        """For initialization of graph"""
        self.V = V
        self.E = 0
        self.adjacency_list = [[] for i in range(V)]

        """File input for txt file"""
        # for line in fileinput.input():
        #     edge =line.split(" ")
        #     directedEdge = DirectedEdge(edge[0], edge[1], edge[2])
        #     self.addEdge(directedEdge)

    def addEdge(self, edge):
        self.adjacency_list[edge.fromVertex()].append(edge)
        self.E += 1

class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def returnWeight(self):
        return self.weight

    def fromVertex(self):
        return self.v

    def toVertex(self):
        return self.w


# Dijkstras Shortest Path Based on Princeton Algorithms Java Implementation
class DijkstrasSP:
    def __init__(self, V, G, s):
        self.edgeTo = [None] * V
        self.distTo = [math.inf] * V
        self.pq = IndexMinPQ(V) # Binary heap PQ
        self.G = G

        self.distTo[s] = 0
        self.pq.insert(s, 0.0)

        while self.pq.is_empty() == False:
            self.relax(self.pq.delete_min())

        for edge in self.edgeTo:
            if edge is not None:
                print(edge.fromVertex(), "->", edge.toVertex(), " ", edge.returnWeight())

    def relax(self, vertex):
        for edge in self.G.adjacency_list[vertex]:
            w = edge.toVertex()
            print("Vertex, Distance Value, Weight of Edge", vertex, self.distTo[vertex], edge.returnWeight())
            if self.distTo[w] > self.distTo[vertex] + edge.returnWeight():
                self.distTo[w] = self.distTo[vertex] + edge.returnWeight()
                self.edgeTo[w] = edge
                if self.pq.contains(w):
                    self.pq.change_key(w, self.distTo[w])
                else:
                    self.pq.insert(w, self.distTo[w])

graph = EdgeWeightedDiagraph(6)
graph.addEdge(DirectedEdge(0, 4, .38))
graph.addEdge(DirectedEdge(4, 5, .35))
graph.addEdge(DirectedEdge(5, 4, .35))
graph.addEdge(DirectedEdge(5, 1, .32))
graph.addEdge(DirectedEdge(1, 3, .29))

DijkstrasSP(7, graph, 0)
