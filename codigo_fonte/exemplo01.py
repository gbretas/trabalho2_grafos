# -*- coding: utf-8 -*-
# /* 
# Gustavo Torres Bretas Alves
# Matricula: 689655
# Matéria: Teoria dos Grafos e Computabilidade
# Professor: Silvio Jamil Ferzoli Guimarães
# Data: 15/12/2021
# */

from collections import defaultdict
from Graph import CaminhosDisjuntosGrafo

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
g = CaminhosDisjuntosGrafo(grafo)
g.caminhos_disjuntos(origem, destino)

print("\n_______\n")