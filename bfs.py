from collections import deque

# time complexity: O(N). We have to visit every node
# space complexity: O(N). Worst case happens when there is a level contains N - 1 nodes.
def bfs_level(source, tree_graph):
    # return a list of lists. Each sublist contains all nodes within a level.
    result = []

    queue = deque([source])
    while queue:
        current_level_size = len(queue)
        level = []

        for i in range(current_level_size):
            node = queue.popleft()
            level.append(node)
            for neighbor in tree_graph[node]:
                queue.append(neighbor)

        result.append(level)

    return result

# time complexity: O(M + N) visit N nodes, and M neighbor edges.
# space complexity: O(N) to store N nodes in queue

def bfs(source, graph):
    # return a list of nodes in visiting order
    result = []

    queue = deque([source])
    visited = set()
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result