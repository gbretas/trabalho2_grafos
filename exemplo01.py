# -*- coding: utf-8 -*-
from collections import defaultdict
from Graph import Graph

print(" == Exemplo 01 == ")
# A -> C
# C -> B
# C -> D
# B -> D

grafo = [
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]

origem = 0
destino = 3
g = Graph(grafo)
g.caminhos_disjuntos(origem, destino)

print("\n_______\n")