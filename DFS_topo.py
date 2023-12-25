# Python program to print topological sorting of a Directed Acyclic Graph (DAG)
from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topological_sort_util(self, v, visited, stack):
        # Mark the current node as visited.
        visited[v] = True
        print(v, " is visited")

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                print("send ", i, " (which is connected to ",
                      v, " ) to topological sort until")
                self.topological_sort_util(i, visited, stack)
        # Push current vertex to stack which stores result
        print("add ", v, " to front of topological order")
        stack.insert(0, v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topological_sort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                print("send ", i, " to topological sort until")
                self.topological_sort_util(i, visited, stack)
        # Print contents of stack
        print(stack)


"""
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.add_edge(3, 0)
print("Following is a Topological Sort of the given graph")
g.topological_sort()
"""
ge = Graph(6)
ge.add_edge(0, 1)
ge.add_edge(0, 2)
ge.add_edge(2, 1)
ge.add_edge(2, 3)
ge.add_edge(2, 4)
ge.add_edge(4, 3)
ge.add_edge(5, 0)
ge.add_edge(5, 3)
print("Following is a Topological Sort of the given ge graph")
ge.topological_sort()
