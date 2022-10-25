import igraph as ig
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

graph = ig.Graph.Read_Pickle("data/ogbn-arxiv.pickle")


def task1():
    print(f"Vertex count: {graph.vcount()}")
    print(f"Edge count: {graph.ecount()}")

    citations = np.array(graph.degree(graph.vs, mode="in"))
    most_citation_count = np.max(citations)
    # FIXME this should probably use np.indices instead of np.arange
    most_citation_indices = np.arange(*citations.shape)[citations == most_citation_count]
    print(f"The papers with the most citations are in subject classes: {graph.vs[most_citation_indices]['label']}")
    print(f"They have {most_citation_count} citations")

    # Now we get the subject of the papers citing the above paper
    _papers_edges = np.array([graph.incident(v, mode="in") for v in most_citation_indices]).flatten()
    papers_edges = graph.es.select(_papers_edges)
    # The source is the paper that is citing the target
    papers = np.array([edge.source for edge in papers_edges])
    subjects = np.array(graph.vs[papers]["label"]).squeeze()
    # TODO account for tha fact that multiple subjects can have the same amount
    binned_subjects = np.bincount(subjects)
    most_popular_subject_count = np.max(binned_subjects)
    most_popular_subjects = np.arange(*binned_subjects.shape)[binned_subjects == most_popular_subject_count]
    print(f"The subject area that most papers that cite the above paper belong to is {most_popular_subjects}")


def task2():
    v_1 = graph.vs.select(year_lt=2019)

    v_2 = graph.vs.select(year_ge=2019)


def task3():
    undir_graph = graph
    undir_graph.to_undirected()

    triangles = np.array([undir_graph.induced_subgraph(undir_graph.neighbors(v)).ecount() for v in undir_graph.vs])
    print(triangles)


def task4():
    for v in graph.vs:
        v.degree()
        v.pagerank(damping=0.85)
        v.coreness(2)
        v.eigenvector_centrality()


def task5():
    v_1 = graph.vs.select(year_lt=2019)

    dataset = np.array(graph.vs['attr'])
    print(dataset)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(dataset, v_1['attr'])


if __name__ == "__main__":
    # task1()
    # task2()
    # task3()
    task5()
