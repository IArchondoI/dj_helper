from src.key_assignment.key_assignment import assign_random_keys
from src.graph_builder.graph_builder import build_harmonic_graph


def test_full_pipeline():
    """
    Test the full pipeline with a small set of inputs.
    """
    # Input songs
    songs = ["Song A", "Song B", "Song C"]

    # Step 1: Assign random keys
    songs_with_keys = assign_random_keys(songs)

    # Step 2: Build harmonic graph
    graph = build_harmonic_graph(songs_with_keys)

    # Assertions
    assert len(graph.nodes) == len(songs)
    assert len(graph.edges) >= 0


if __name__ == "__main__":
    test_full_pipeline()
