from src.models.song import Song
from src.key_assignment.key_assignment import assign_keys
from src.graph_builder.graph_builder import build_harmonic_graph


def test_full_pipeline():
    """
    Test the full pipeline with a small set of inputs.
    """
    # Input songs
    songs = [
        Song(title="Imagine", artist="John Lennon"),
        Song(title="Hotel California", artist="Eagles"),
        Song(title="Hey Jude", artist="The Beatles"),
    ]

    # Toggle to use Spotipy for key and BPM assignment
    use_spotipy = False

    # Step 1: Assign keys
    evaluated_songs = assign_keys(songs, use_spotipy)

    # Step 2: Build harmonic graph
    graph = build_harmonic_graph(evaluated_songs)

    # Assertions
    assert len(graph.nodes) == len(songs)
    assert len(graph.edges) >= 0
