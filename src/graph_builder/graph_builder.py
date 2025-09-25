import networkx as nx
from typing import List
from src.camelot_wheel.camelot_wheel import is_harmonically_compatible
from src.models.evaluated_song import EvaluatedSong


def build_harmonic_graph(songs: List[EvaluatedSong]) -> nx.Graph:
    """
    Builds a graph where nodes are songs and edges harmonic compatibility.
    """

    graph = nx.Graph()

    # Add nodes
    for song in songs:
        graph.add_node(song.title, key=song.key, bpm=song.bpm)

    # Add edges based on compatibility
    for i, song1 in enumerate(songs):
        for j, song2 in enumerate(songs):
            if i < j and is_harmonically_compatible(
                song1.key.value, song2.key.value
            ):
                graph.add_edge(song1.title, song2.title)

    return graph
