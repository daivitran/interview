import heapq

# Time complexity: O((V+E)logV).
# Space: O(V)
def dijkstra(source, graph):
    # graph[u].keys() return a list of nodes that u points to,
    # graph[u][v] returns the weight from u to v.

    dist = dict()
    prev = dict()
    for vertex in graph.keys():
        dist[vertex] = float("inf")
        prev[vertex] = None
    dist[source] = 0

    heap = []
    for vertex in graph.keys():
        heapq.heappush(heap, (dist[vertex], vertex))
    visited = dict()
    while heap:
        node = heapq.heappop(heap) # happens at most V times
        visited[node] = True
        for neighbor in graph[node].keys(): # happens at most E times.
            if visited[neighbor]:
                continue
            if dist[node] + graph[node][neighbor] < dist[neighbor]:
                dist[neighbor] = dist[node] + graph[node][neighbor]
                prev[neighbor] = node
                heapq.heappush(heap, (dist[neighbor], neighbor))

    return dist, prev