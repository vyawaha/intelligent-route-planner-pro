import heapq

def dijkstra(G, start, end, weight="distance"):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        path = path + [node]

        if node == end:
            return path, cost

        for neighbor in G[node]:
            if neighbor not in visited:
                new_cost = cost + G[node][neighbor][weight]
                heapq.heappush(pq, (new_cost, neighbor, path))

    return [], float("inf")


def a_star(G, start, end):
    import math

    def heuristic(a, b):
        ax, ay = G.nodes[a]["pos"]
        bx, by = G.nodes[b]["pos"]
        return abs(ax-bx) + abs(ay-by)

    pq = [(0, start, [], 0)]
    visited = set()

    while pq:
        f, node, path, g = heapq.heappop(pq)

        if node == end:
            return path + [node], g

        if node in visited:
            continue
        visited.add(node)

        path = path + [node]

        for n in G[node]:
            if n not in visited:
                new_g = g + G[node][n]["time"]
                new_f = new_g + heuristic(n, end)
                heapq.heappush(pq, (new_f, n, path, new_g))

    return [], float("inf")