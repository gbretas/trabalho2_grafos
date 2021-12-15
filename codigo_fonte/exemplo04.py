# -*- coding: utf-8 -*-
# /* 
# Gustavo Torres Bretas Alves
# Matricula: 689655
# Matéria: Terioa Geral de Grafos e Computabilidade
# Professor: Silvio Jamil Ferzoli Guimarães
# Data: 15/12/2021
# */

from collections import defaultdict
from Graph import CaminhosDisjuntosGrafo

print(" == Exemplo 04 == ")
# 0 -> 1
# 0 -> 2
# 0 -> 3

# 1 -> 2

# 2 -> 3
# 2 -> 6

# 3 -> 6

# 4 -> 2
# 4 -> 7

# 5 -> 4
# 5 -> 1
# 5 -> 7

# 6 -> 5
# 6 -> 7

grafo = [
#    0, 1, 2, 3, 4, 5, 6, 7
    [0, 1, 1, 1, 0, 0, 0, 0], # 0
    [0, 0, 1, 0, 0, 0, 0, 0], # 1
    [0, 0, 0, 1, 0, 0, 1, 0], # 2
    [0, 0, 0, 0, 0, 0, 1, 0], # 3
    [0, 0, 1, 0, 0, 0, 0, 1], # 4
    [0, 1, 0, 0, 1, 0, 0, 1], # 5
    [0, 0, 0, 0, 0, 1, 0, 1], # 6
    [0, 0, 0, 0, 0, 0, 0, 0]  # 7
]

origem = 0
destino = 7
g = CaminhosDisjuntosGrafo(grafo)
g.caminhos_disjuntos(origem, destino)

print("\n_______\n")