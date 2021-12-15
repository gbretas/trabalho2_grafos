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

print(" == Exemplo 03 == ")
# A -> B
# A -> C
# A -> E
# A -> D
# B -> D
# B -> F
# B -> H
# C -> B
# C -> D
# C -> G
# D -> E
# E -> H
# F -> H
# G -> H

grafo = [
#    A  B  C  D  E  F  G  H
    [0, 1, 1, 1, 1, 0, 0, 0], # A
    [0, 0, 0, 1, 0, 1, 0, 1], # B
    [0, 1, 0, 1, 0, 0, 1, 0], # C
    [0, 0, 0, 0, 1, 0, 0, 0], # D
    [0, 0, 0, 0, 0, 0, 0, 1], # E
    [0, 0, 0, 0, 0, 0, 0, 1], # F
    [0, 0, 0, 0, 0, 0, 0, 1], # G
    [0, 0, 0, 0, 0, 0, 0, 0]  # H
]

origem = 0
destino = 7
g = CaminhosDisjuntosGrafo(grafo)
g.caminhos_disjuntos(origem, destino)

print("\n_______\n")