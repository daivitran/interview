"""
Building a graph usually requires a list of edges and number of nodes.
"""
def build_adjacency_list_directed(n, directedEdges):
    graph = dict()

    for i in range(n):
        graph[i] = []

    for edge in directedEdges:
        graph[edge[0]].append(edge[1])
    return graph

def build_adjacency_list_undirected(n, undirectedEdges):
    graph = dict()

    for i in range(n):
        graph[i] = []

    for edge in undirectedEdges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph

"""
Singly Linked List Node
"""
class SLListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

"""
Tree Node
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right