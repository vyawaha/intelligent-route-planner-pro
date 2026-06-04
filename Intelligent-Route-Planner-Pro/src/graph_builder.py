import networkx as nx
import random

def create_city_graph(n=10):
    G = nx.Graph()

    for i in range(n):
        for j in range(n):
            node = f"N{i}_{j}"
            G.add_node(node, pos=(i, j))

    for i in range(n):
        for j in range(n):
            if j < n-1:
                a, b = f"N{i}_{j}", f"N{i}_{j+1}"
                w = random.randint(1, 10)
                G.add_edge(a, b, distance=w, time=w*2, toll=random.randint(0, 5))

            if i < n-1:
                a, b = f"N{i}_{j}", f"N{i+1}_{j}"
                w = random.randint(1, 10)
                G.add_edge(a, b, distance=w, time=w*2, toll=random.randint(0, 5))

    return G