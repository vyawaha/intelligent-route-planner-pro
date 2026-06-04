import matplotlib.pyplot as plt
import networkx as nx


def draw_traffic_heatmap(
    G,
    filename="outputs/traffic_heatmap.png"
):
    pos = nx.get_node_attributes(G, "pos")

    plt.figure(figsize=(12, 8))

    edge_colors = []

    for u, v in G.edges():

        traffic = G[u][v]["time"]

        if traffic < 8:
            edge_colors.append("#00AA00")      # Dark Green

        elif traffic < 15:
            edge_colors.append("#FF8800")      # Bright Orange

        else:
            edge_colors.append("#CC0000")      # Dark Red

    nx.draw(
        G,
        pos,
        node_size=250,
        node_color="lightgray",
        edge_color=edge_colors,
        width=3,
        with_labels=True,
        font_size=7
    )

    labels = nx.get_edge_attributes(G, "time")

    rounded_labels = {}

    for edge, value in labels.items():
        rounded_labels[edge] = round(value, 1)

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=rounded_labels,
        font_size=6
    )

    plt.title(
        "Traffic Heatmap Visualization",
        fontsize=16,
        fontweight="bold"
    )

    plt.axis("off")

    plt.savefig(
        filename,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"[SAVED] {filename}")