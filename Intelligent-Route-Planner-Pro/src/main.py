from graph_builder import create_city_graph
from traffic_simulator import apply_traffic

from algorithms import dijkstra, a_star

from visualizer import draw_graph

from traffic_visualizer import draw_traffic_heatmap

from comparison_visualizer import draw_route_comparison

from report_generator import generate_report

from metrics import save_metrics


def main():

    print("\n==============================")
    print("INTELLIGENT ROUTE PLANNER PRO")
    print("==============================")

    # Create graph
    G = create_city_graph()

    print("\n[SUCCESS] City graph generated")

    # Apply traffic simulation
    apply_traffic(G)

    print("[SUCCESS] Traffic simulation applied")

    source = "N0_0"
    destination = "N9_9"

    print(f"\nSource      : {source}")
    print(f"Destination : {destination}")

    # Dijkstra Route
    print("\nRunning Dijkstra...")

    dijkstra_path, dijkstra_cost = dijkstra(
        G,
        source,
        destination,
        "distance"
    )

    # A* Route
    print("Running A* Search...")

    astar_path, astar_cost = a_star(
        G,
        source,
        destination
    )

    print("\n========== RESULTS ==========")

    print("\nDijkstra Route:")
    print(dijkstra_path)

    print("\nDijkstra Cost:")
    print(round(dijkstra_cost, 2))

    print("\nA* Route:")
    print(astar_path)

    print("\nA* Cost:")
    print(round(astar_cost, 2))

    print("\nGenerating Visualizations...")

    # Main Route Visualization
    draw_graph(
        G,
        astar_path,
        "outputs/graph.png"
    )

    # Traffic Heatmap
    draw_traffic_heatmap(
        G,
        "outputs/traffic_heatmap.png"
    )

    # Route Comparison
    draw_route_comparison(
        G,
        dijkstra_path,
        astar_path,
        "outputs/route_comparison.png"
    )

    # Route Report
    generate_report(
        astar_path,
        astar_cost,
        "outputs/report.txt"
    )

    # Metrics Report
    save_metrics(
        dijkstra_cost,
        astar_cost,
        "outputs/metrics.txt"
    )

    print("\n==============================")
    print("ALL OUTPUTS GENERATED")
    print("==============================")

    print("\nGenerated Files:")

    print("outputs/graph.png")
    print("outputs/traffic_heatmap.png")
    print("outputs/route_comparison.png")
    print("outputs/report.txt")
    print("outputs/metrics.txt")

    print("\nProject execution completed successfully.")


if __name__ == "__main__":
    main()