import igraph as ig
import numpy as np


graph = ig.Graph.Read_Pickle("data/ogbn-arxiv.pickle")


def task1():
    print(f"Vertex count: {len(graph.vs)}")
    print(f"Edge count: {len(graph.es)}")

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
    smaller_mask = np.array(graph.vs["year"]) < 2019
    v_1 = graph.vs.select(smaller_mask.squeeze().nonzero())
    v_2 = graph.vs.select((not smaller_mask).squeeze().nonzero())


if __name__ == "__main__":
    task1()
    task2()
