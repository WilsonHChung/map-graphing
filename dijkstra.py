import sys


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def print(self, distance):
        print
        for node in range(self.V):
            print
            node, "t", distance[node]

            # A utility function to find the vertex with

    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minD(self, distance, shortPathSet):

        # Initilaize minimum distance for next node
        min = sys.maxint

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if distance[v] < min and shortPathSet[v] == False:
                min = distance[v]
                index = v

        return index

        # Funtion that implements Dijkstra's single source

    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        distance = [sys.maxint] * self.V
        shortPathSet = [False] * self.V
        distance[src] = 0
        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minD(distance, shortPathSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            shortPathSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and shortPathSet[v] == False and distance[v] > distance[u] + self.graph[u][v]:
                    distance[v] = distance[u] + self.graph[u][v]

        self.print(distance)


# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

g.dijkstra(0);

