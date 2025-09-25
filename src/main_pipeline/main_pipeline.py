from src.key_assignment.key_assignment import assign_random_keys
from src.graph_builder.graph_builder import build_harmonic_graph


def main():
    """
    Main pipeline to assign keys, determine compatibility, and build a graph.
    """
    # Example input songs
    songs = ["Song A", "Song B", "Song C", "Song D"]

    # Step 1: Assign random keys
    songs_with_keys = assign_random_keys(songs)

    # Step 2: Build harmonic graph
    graph = build_harmonic_graph(songs_with_keys)

    # Output the graph
    print("Nodes:", graph.nodes(data=True))
    print("Edges:", graph.edges())


if __name__ == "__main__":
    main()
