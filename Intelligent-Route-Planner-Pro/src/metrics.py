def save_metrics(
    dijkstra_cost,
    astar_cost,
    filename="outputs/metrics.txt"
):

    with open(filename, "w") as f:

        f.write("ROUTE ANALYTICS\n")
        f.write("====================\n")

        f.write(
            f"Dijkstra Cost: {dijkstra_cost}\n"
        )

        f.write(
            f"A* Cost: {astar_cost}\n"
        )

        improvement = (
            dijkstra_cost - astar_cost
        )

        f.write(
            f"Difference: {improvement}\n"
        )

    print(f"[SAVED] {filename}")