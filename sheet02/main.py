import igraph as ig
import numpy as np

dir_graph = undir_graph = ig.Graph.Read_Pickle("../sheet01/data/ogbn-arxiv.pickle")
undir_graph = undir_graph.as_undirected()


def count_paths_with_k_length_from_vertex(base_vid, graph, k):
    stack = [(base_vid, graph.neighbors(base_vid))]
    paths = []
    parents = [base_vid]

    # go down the rabbit hole
    while stack:
        vid, neighbors = stack[-1]
        if neighbors and len(parents) <= k:
            # Get next neighbor to visit
            neighbor = neighbors.pop()
            if neighbor not in parents:
                # Add hanging subtree neighbor
                stack.append((neighbor, graph.neighbors(neighbor)))
                # append the newly added neighbor to the parents path
                parents.append(neighbor)
        else:
            # check if the path that just ended was long enough
            if len(parents) == k+1:
                paths.append(parents)

            # because we use the stack the current parents path has to be reduced by one as the last vertex
            # in the reduced list is the next observed after popping the current vertex off the stack
            parents = parents[0:-1]
            stack.pop()

    print(f"paths: {paths}")

    return len(paths)


def count_paths_with_k_length(k, graph=undir_graph):
    for i, v in enumerate(graph.vs):
        print(f"Vertex: {v.index}, Number of paths with length {k-1}:"
              f" {count_paths_with_k_length_from_vertex(v.index, graph, k - 1)}")
        if i > 100:
            exit()


def task1_1():
    count_paths_with_k_length(3)
    count_paths_with_k_length(4)
    count_paths_with_k_length(5)


def task1_2():
    first_graph = ig.Graph(n=4, edges=[(0, 1), (1, 2), (2, 3), (1, 3)])
    second_graph = ig.Graph(n=4, edges=[(0, 1), (1, 2), (2, 3), (1, 3), (0, 3)])
    third_graph = ig.Graph(n=5, edges=[(0, 1), (1, 2), (2, 3), (0, 3), (1, 4), (2, 4)])
    fourth_graph = ig.Graph(n=5, edges=[(0, 1), (1, 2), (2, 3), (0, 3), (3, 4), (2, 0)])
    fifth_graph = ig.Graph(n=5, edges=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2), (1, 3), (1, 4)])

    print("first graph")
    count_paths_with_k_length(3, first_graph)
    count_paths_with_k_length(4, first_graph)
    count_paths_with_k_length(5, first_graph)
    print("second graph")
    count_paths_with_k_length(3, second_graph)
    count_paths_with_k_length(4, second_graph)
    count_paths_with_k_length(5, second_graph)
    print("third graph")
    count_paths_with_k_length(3, third_graph)
    count_paths_with_k_length(4, third_graph)
    count_paths_with_k_length(5, third_graph)
    print("fourth graph")
    count_paths_with_k_length(3, fourth_graph)
    count_paths_with_k_length(4, fourth_graph)
    count_paths_with_k_length(5, fourth_graph)
    print("fifth graph")
    count_paths_with_k_length(3, fifth_graph)
    count_paths_with_k_length(4, fifth_graph)
    count_paths_with_k_length(5, fifth_graph)


if __name__ == '__main__':
    # task1_1()
    task1_2()
