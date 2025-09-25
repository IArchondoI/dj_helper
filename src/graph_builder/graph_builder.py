import networkx as nx
from typing import List, Dict
from src.camelot_wheel.camelot_wheel import is_harmonically_compatible


def build_harmonic_graph(songs: List[Dict[str, str]]) -> nx.Graph:
    """
    Builds a graph where nodes are songs and edges harmonic compatibility.
    """

    graph = nx.Graph()

    # Add nodes
    for song in songs:
        graph.add_node(song["song"], key=song["key"])

    # Add edges based on compatibility
    for i, song1 in enumerate(songs):
        for j, song2 in enumerate(songs):
            if i < j and is_harmonically_compatible(
                song1["key"], song2["key"]
            ):
                graph.add_edge(song1["song"], song2["song"])

    return graph
