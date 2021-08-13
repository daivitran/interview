from utils import *
from strongly_connected_components import *

if __name__ == "__main__":
    print("Interview ALgorithms")

    # prepare arguments
    n = 3
    edges = [[0,1], [1,2], [2,0]]
    graph = build_adjacency_list_directed(n, edges)

    # find scc_num

    print(compress_graph(graph))