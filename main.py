from src.key_assignment.key_assignment import assign_keys
from src.graph_builder.graph_builder import build_harmonic_graph
from src.graph_builder.graph_visualizer import visualize_graph
from src.utils.csv_reader import load_songs_from_csv
import sys
from pathlib import Path


# Toggle to use Mistral for key and BPM assignment
use_mistral = False


def main(songs_path: Path):
    """
    Main function to execute the pipeline for harmonic graph visualization.
    """
    # Load songs from CSV
    songs, evaluated_songs = load_songs_from_csv(songs_path)

    # Assign keys to songs without key and BPM
    evaluated_songs.extend(assign_keys(songs, use_mistral))

    # Step 2: Build harmonic graph
    graph = build_harmonic_graph(evaluated_songs)

    # Step 3: Visualize the graph
    visualize_graph(graph)


if __name__ == "__main__":
    csv_file_path = (
        sys.argv[1] if len(sys.argv) > 1 else "tests/dummy_songs.csv"
    )
    main(Path(csv_file_path))
