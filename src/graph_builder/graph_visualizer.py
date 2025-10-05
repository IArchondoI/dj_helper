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

    # Prepare labels for the graph nodes with BPM
    labels = {}
    for node, data in graph.nodes(data=True):
        title = node
        key = (
            str(data.get("key", "")).replace("_SHARP", "#").replace("Key.", "")
        )
        bpm = data.get("bpm", "")
        labels[node] = f"{title}\n{key}\n{bpm}"

    # Define edge colors and widths based on BPM differences
    edge_colors = []
    edge_widths = []
    for u, v in graph.edges():
        bpm_diff = abs(graph.nodes[u]["bpm"] - graph.nodes[v]["bpm"])
        if bpm_diff <= 6:
            edge_colors.append("green")
        elif bpm_diff <= 20:
            edge_colors.append("yellow")
        else:
            edge_colors.append("red")
        edge_widths.append(2.0)  # Make edges fatter

    # Adjust layout to spread nodes even further apart
    pos = nx.spring_layout(graph, k=1.0)  # Increase `k` to spread nodes more

    # Update edge colors: yellow -> orange
    edge_colors = [
        "orange" if color == "yellow" else color for color in edge_colors
    ]

    # Draw the graph with labels and colored edges
    plt.figure(figsize=(14, 12))
    ax = plt.gca()
    ax.set_facecolor("black")  # Ensure the background is set to black
    nx.draw(
        graph,
        pos=pos,
        labels=labels,
        node_color="lightblue",
        edge_color=edge_colors,
        width=edge_widths,
        node_size=2000,
        font_size=10,
        font_color="black",  # Set text color to black
        with_labels=True,
    )

    # Save the graph as an image
    plt.savefig(filename)
    plt.close()

    print(f"Graph saved as {filename}")
