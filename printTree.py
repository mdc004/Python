import matplotlib.pyplot as plt
import networkx as nx


# Creazione di un albero binario di altezza 4 con un layout gerarchico manuale
tree = nx.DiGraph()

# Nodi e archi per un albero binario
nodes = [
    (1, "A"), (2, "B"), (3, "C"), (4, "D"), (5, "E"), (6, "F"), (7, "G"), 
    (8, "H"), (9, "I"), (10, "J"), (11, "K"), (12, "L"), (13, "M"), (14, "N"), (15, "O")
]
edges = [
    (1, 2), (1, 3),  # Livello 1
    (2, 4), (2, 5), (3, 6), (3, 7),  # Livello 2
    (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13), (7, 14), (7, 15)  # Livello 3
]

# Aggiunta nodi e archi
tree.add_nodes_from([n[0] for n in nodes])
tree.add_edges_from(edges)

# Posizioni definite manualmente per simulare un layout gerarchico
pos = {
    1: (0, 4),  # Livello 0
    2: (-2, 3), 3: (2, 3),  # Livello 1
    4: (-3, 2), 5: (-1, 2), 6: (1, 2), 7: (3, 2),  # Livello 2
    8: (-3.5, 1), 9: (-2.5, 1), 10: (-1.5, 1), 11: (-0.5, 1),
    12: (0.5, 1), 13: (1.5, 1), 14: (2.5, 1), 15: (3.5, 1)  # Livello 3
}

# Disegno dell'albero binario
labels = {node[0]: node[1] for node in nodes}
plt.figure(figsize=(12, 8))
nx.draw(tree, pos, with_labels=True, labels=labels, node_color="lightblue", node_size=1500, font_size=10, font_weight="bold", edge_color="gray")
plt.title("Albero binario di altezza 4")
plt.show()
