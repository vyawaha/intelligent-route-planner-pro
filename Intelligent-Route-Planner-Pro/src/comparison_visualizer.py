import matplotlib.pyplot as plt
import networkx as nx


def draw_route_comparison(
    G,
    dijkstra_path,
    astar_path,
    filename="outputs/route_comparison.png"
):

    pos = nx.get_node_attributes(G, "pos")

    plt.figure(figsize=(12, 8))

    nx.draw(
        G,
        pos,
        node_size=250,
        node_color="lightgray",
        edge_color="silver",
        width=1,
        with_labels=True,
        font_size=7
    )

    dijkstra_edges = list(
        zip(
            dijkstra_path,
            dijkstra_path[1:]
        )
    )

    astar_edges = list(
        zip(
            astar_path,
            astar_path[1:]
        )
    )

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=dijkstra_edges,
        width=5,
        edge_color="#0033CC"
    )

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=astar_edges,
        width=5,
        edge_color="#CC0000"
    )

    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=[dijkstra_path[0]],
        node_color="green",
        node_size=500
    )

    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=[dijkstra_path[-1]],
        node_color="red",
        node_size=500
    )

    plt.title(
        "Route Comparison (Blue = Dijkstra | Red = A*)",
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