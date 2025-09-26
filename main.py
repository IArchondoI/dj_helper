from src.models.song import Song
from src.key_assignment.key_assignment import assign_keys
from src.graph_builder.graph_builder import build_harmonic_graph
from src.graph_builder.graph_visualizer import visualize_graph


def main():
    """
    Main function to execute the pipeline for harmonic graph visualization.
    """
    songs = [
        Song(title="Bohemian Rhapsody", artist="Queen"),
        Song(title="Billie Jean", artist="Michael Jackson"),
        Song(title="Smells Like Teen Spirit", artist="Nirvana"),
    ]

    # Toggle to use Spotipy for key and BPM assignment
    use_spotipy = True

    # Step 1: Assign keys
    evaluated_songs = assign_keys(songs, use_spotipy)

    # Step 2: Build harmonic graph
    graph = build_harmonic_graph(evaluated_songs)

    # Step 3: Visualize the graph
    visualize_graph(graph)


if __name__ == "__main__":
    main()
