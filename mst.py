import heapq

from disjointset import DisjointSet

# Time: O(ElogE)
# Space: O(E)
def kruskal(n, edges):
    # edge = [v1, v2, weight]. n is number of nodes. assume nodes are labelled from 0 to n -1
    dsu = DisjointSet(n)

    heap = []
    for edge in edges:
        heapq.heappush(heap, (edge[2], (edge[0], edge[1])))

    result = []
    while heap:
        weight, edge = heapq.heappop()
        if not dsu.is_connected(edge[0], edge[1]):
            result.append(edge)
            dsu.union(edge[0], edge[1])

    return result



def prim():
   pass