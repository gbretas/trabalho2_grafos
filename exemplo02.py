# -*- coding: utf-8 -*-
from collections import defaultdict
from Graph import Graph

print(" == Exemplo 02 == ")
# A -> B
# A -> C
# B -> C
# B -> D
# C -> D


grafo = [
#    A  B  C  D
    [0, 1, 1, 0], # A
    [0, 0, 1, 1], # B
    [0, 0, 0, 1], # C
    [0, 0, 0, 0]  # D
]

origem = 0
destino = 3
g = Graph(grafo)
g.caminhos_disjuntos(origem, destino)

print("\n_______\n")