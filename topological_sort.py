# Topological sort is applied to Directed Acyclic Graph to
# find a a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u
# comes before v in the ordering
from utils import build_adjacency_list_directed
from collections import deque

# time complexity: O(N+M)
# space: O(N)
def topological_sort(total_nodes, edges):
    # build graph
    graph = build_adjacency_list_directed(total_nodes, edges)

    # calculate the indegree of all nodes
    indegrees = dict()
    for node in graph.keys():
        indegrees[node] = 0

    for node in graph.keys():
        for neighbor in graph[node]:
            indegrees[neighbor] += 1

    # find nodes with indegree == 0
    queue = deque([])
    for node in graph.keys():
        if indegrees[node] == 0:
            queue.append(node)

    result = []
    while queue:
        node = deque.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph.keys()):
        # there is a cycle
        return []

    return result
