# Source: https://cs170.org/assets/notes/Lecture%206.pdf

"""
Graph Compression
"""
def compress_graph(graph):
    scc, vertex_to_scc = find_scc(graph)

    compressed_graph = dict()
    for i in range(scc):
        compressed_graph[i] = set()
    visited = set()

    def dfs(n):
        visited.add(n)
        for neighbor in graph[n]:
            start_scc = vertex_to_scc[n]
            end_scc = vertex_to_scc[neighbor]
            if start_scc != end_scc: # not in the same component
                compressed_graph[start_scc].add(end_scc)
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph.keys():
        if node not in visited:
            dfs(node)

    for i in range(scc):
        compressed_graph[i] = list(compressed_graph[i])

    return compressed_graph




"""
Strongly Connected Components Finder
"""
# get a mapping from node to its corresponding strongly connected component
def find_scc(graph):
    scc = 0
    scc_num = dict()
    r_graph = reverse_graph(graph)
    descending_post_orders = find_descending_post_order(r_graph)

    visited = set()

    def dfs(n):
        visited.add(n)
        scc_num[n] = scc
        for neighbor in graph[n]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in descending_post_orders:
        if node not in visited:
            dfs(node)
            scc += 1

    return scc, scc_num


# Time complexity: O(M+N)
def reverse_graph(graph):
    r_graph = dict()
    for node in graph.keys():
        r_graph[node] = []

    for node in graph.keys():
        for neighbor in graph[node]:
            r_graph[neighbor].append(node)

    return r_graph


# Time complexity: O(M+N)
def find_descending_post_order(graph):
    ascending_post_orders = []
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        ascending_post_orders.append(node)

    for node in graph.keys():
        if node not in visited:
            dfs(node)

    return list(reversed(ascending_post_orders))
