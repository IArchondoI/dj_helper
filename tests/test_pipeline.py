from src.key_assignment.key_assignment import assign_keys
from src.graph_builder.graph_builder import build_harmonic_graph
from src.utils.csv_reader import load_songs_from_csv


def test_full_pipeline_with_csv():
    """
    Test the full pipeline with a CSV input.
    """
    # Load songs from CSV
    csv_path = "tests/dummy_songs.csv"
    # Separate unevaluated and evaluated songs
    unevaluated_songs, evaluated_songs = load_songs_from_csv(csv_path)

    # Toggle to use Spotipy for key and BPM assignment
    use_spotipy = False

    # Assign keys to unevaluated songs
    evaluated_songs.extend(assign_keys(unevaluated_songs, use_spotipy))

    # Step 2: Build harmonic graph
    graph = build_harmonic_graph(evaluated_songs)

    # Assertions
    assert len(graph.nodes) == len(evaluated_songs)
    assert len(graph.edges) >= 0
