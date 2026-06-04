import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(G, path=None, filename="outputs/graph.png"):
    pos = nx.get_node_attributes(G, "pos")

    plt.figure(figsize=(10, 8))

    # -------------------------
    # BASE GRAPH (FADED)
    # -------------------------
    nx.draw(
        G,
        pos,
        node_size=120,
        node_color="lightgray",
        edge_color="lightgray",
        alpha=0.5
    )

    # -------------------------
    # DRAW PATH (HIGHLIGHTED)
    # -------------------------
    if path:
        edges = list(zip(path, path[1:]))

        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=path,
            node_color="orange",
            node_size=300
        )

        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=[path[0]],
            node_color="green",
            node_size=400
        )

        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=[path[-1]],
            node_color="red",
            node_size=400
        )

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=edges,
            edge_color="red",
            width=3
        )

        nx.draw_networkx_labels(G, pos, font_size=8, font_color="black")

    # -------------------------
    # FINAL POLISH
    # -------------------------
    plt.title("Intelligent Route Planner - Optimal Path Visualization")
    plt.axis("off")

    plt.savefig(filename, dpi=200, bbox_inches="tight")
    plt.close()

    print(f"[SAVED] Enhanced Graph Visualization → {filename}")