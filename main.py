from src.models.song import Song
from src.key_assignment.key_assignment import assign_random_keys
from src.graph_builder.graph_builder import build_harmonic_graph
from src.graph_builder.graph_visualizer import visualize_graph


def main():
    """
    Main function to execute the pipeline for harmonic graph visualization.
    """
    songs = [
        Song(title="Song A", artist="Artist A"),
        Song(title="Song B", artist="Artist B"),
        Song(title="Song C", artist="Artist C"),
    ]

    # Step 1: Assign random keys
    evaluated_songs = assign_random_keys(songs)

    # Step 2: Build harmonic graph
    graph = build_harmonic_graph(evaluated_songs)

    # Step 3: Visualize the graph
    visualize_graph(graph)


if __name__ == "__main__":
    main()
