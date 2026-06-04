import random

def apply_traffic(G):
    for u, v in G.edges():
        factor = random.uniform(1.0, 2.0)
        G[u][v]["time"] *= factor