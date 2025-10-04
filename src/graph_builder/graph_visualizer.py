import matplotlib.pyplot as plt
import os
import time
import networkx as nx


def visualize_graph(graph):
    """
    Visualize the graph and save it as an image in the outputs folder.
    """
    # Create the outputs directory if it doesn't exist
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Generate a timestamped filename
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(output_dir, f"graph_{timestamp}.png")

    # Prepare labels for the graph nodes
    labels = {}
    for node, data in graph.nodes(data=True):
        title = node
        key = (
            str(data.get("key", "")).replace("_SHARP", "#").replace("Key.", "")
        )
        labels[node] = f"{title}\n{key}"

    # Adjust layout to spread nodes further apart
    pos = nx.spring_layout(graph, k=0.5)  # Increase `k` to spread nodes

    # Draw the graph with labels
    plt.figure(figsize=(12, 10))
    nx.draw(
        graph,
        pos=pos,
        labels=labels,
        node_color="lightblue",
        edge_color="gray",
        node_size=2000,
        font_size=10,
        with_labels=True,
    )

    # Save the graph as an image
    plt.savefig(filename)
    plt.close()

    print(f"Graph saved as {filename}")
