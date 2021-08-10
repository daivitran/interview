# time: O(N + M) if source can visited all other graphs.
# space: O(N) for recursive stack
def dfs_recursive(source, graph):
    # find all reachable nodes from the source node in the graph, and return in order of visited

    result = []
    visited = set()
    def dfs(node):
        result.append(node)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(source)
    return result

# time: O(N + M) but Recursive approach is empirically much faster
# space: O(N) for the stack
def dfs_iterative(source, graph):
    # find all reachable nodes from the source node in the graph

    result = []
    stack = [source]
    visited = set()

    while stack:
        node = stack.pop()
        result.append(node)
        visited.append(node)

        for neighbor in source[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return result
