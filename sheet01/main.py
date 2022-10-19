import igraph as ig
import numpy as np


def task1():
    graph = ig.Graph.Read_Pickle('data/ogbn-arxiv.pickle')
    print(f"Amount of vertices: {graph.vcount()}")
    print(f"Amount of edges: {graph.ecount()}")
    # TODO account for the fact that multiple papers can have the same amount of citations
    citations = graph.degree(graph.vs, mode="in")
    most_citations_vertex = np.argsort(citations)[-1]
    print(f"The paper with the most citations is in subject class: {graph.vs['label'][most_citations_vertex]}")

    # Now we get the subject of the papers citing the above paper
    papers = graph.incident(most_citations_vertex, mode="in")
    # TODO this is wrong since Graph.incident only returns the edges but not the vertecies. Maybe use EdgeSeq.target
    subjects = graph.vs[papers]["label"]
    # TODO account for tha fact that multiple subjects can have the same amount
    most_popular_subject = np.argsort(np.bincount(subjects))[-1]
    print(f"The subject area that most papers that cite the above paper belong to is {most_popular_subject}")


def task2():
    pass


def task3():
    pass


def main():
    task1()
