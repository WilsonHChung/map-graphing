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

# Minimum-oriented indexed PQ implementation based on a binary heap

class IndexMinPQ(object):

    def __init__(self, max_size):
        assert max_size > 0
        self._max_size = max_size
        self._index = [-1] * (max_size + 1)
        self._reverse_index = [-1] * (max_size + 1)
        self._keys = [None] * (max_size + 1)
        self._keys_size = 0

    def is_empty(self):
        return self._keys_size == 0

    def size(self):
        return self._keys_size

    def contains(self, index):
        if index >= self._max_size:
            return False
        return self._reverse_index[index] != -1

    def insert(self, index, element):
        if index >= self._max_size or self.contains(index):
            return

        self._keys_size += 1
        self._index[self._keys_size] = index
        self._reverse_index[index] = self._keys_size
        self._keys[index] = element
        self.swim(self._keys_size)

    def min_index(self):
        return None if self._keys_size == 0 else self._index[1]

    def min_key(self):
        return None if self._keys_size == 0 else self._keys[self._index[1]]

    def exchange(self, pos_a, pos_b):
        self._index[pos_a], self._index[pos_b] = self._index[pos_b], self._index[pos_a]
        self._reverse_index[self._index[pos_a]] = pos_a
        self._reverse_index[self._index[pos_b]] = pos_b

    def swim(self, pos):
        while pos > 1 and self._keys[self._index[pos // 2]] > self._keys[self._index[pos]]:
            self.exchange(pos // 2, pos)
            pos //= 2

    def sink(self, pos):
        length = self._keys_size
        while 2 * pos <= length:
            tmp = 2 * pos
            if tmp < length and self._keys[self._index[tmp]] > self._keys[self._index[tmp + 1]]:
                tmp += 1
            if not self._keys[self._index[tmp]] < self._keys[self._index[pos]]:
                break
            self.exchange(tmp, pos)
            pos = tmp

    def change_key(self, i, key):
        if i < 0 or i >= self._max_size or not self.contains(i):
            return
        self._keys[i] = key
        self.swim(self._reverse_index[i])
        self.sink(self._reverse_index[i])

    def delete_min(self):
        if self._keys_size == 0:
            return
        min_index = self._index[1]
        self.exchange(1, self._keys_size)
        self._keys_size -= 1
        self.sink(1)
        self._reverse_index[min_index] = -1
        self._keys[self._index[self._keys_size + 1]] = None
        self._index[self._keys_size + 1] = -1
        return min_index


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



