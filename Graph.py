# -*- coding: utf-8 -*-
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)

    # Utilizar uma BFS como um algoritmo de busca
    def busca_bfs(self, s, t, parent):
        ja_visitado = [False] * (self.ROW)
        lista = []

        lista.append(s)
        ja_visitado[s] = True

        while lista:
            u = lista.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if ja_visitado[ind] == False and val > 0:
                    lista.append(ind)
                    ja_visitado[ind] = True
                    parent[ind] = u


        return True if ja_visitado[t] else False

    # Aplicação do algoritimo do ford fulkerson adaptado para o problema
    # método de resolução deste problema que receba um grafo e um par de vértices
    def caminhos_disjuntos(self, origem, destino):
        parent = [-1] * (self.ROW)
        max_caminhos_disjuntos = 0
        

        while self.busca_bfs(origem, destino, parent):
            original_destino = destino;
            caminho = [];

            path = float("Inf")
            s = destino
            
            while(s != origem):
                path = min(path, self.graph[parent[s]][s])
                s = parent[s]
                caminho.append(s);
            

            # Adicionar o fluxo ao grafo
            # max_caminhos_disjuntos += path
            max_caminhos_disjuntos += 1
            

            # atualizar o grafo residual com o fluxo
            v = destino
            while(v != origem):
                u = parent[v]
                self.graph[u][v] -= path
                self.graph[v][u] += path
                v = parent[v]
            res_caminho = caminho[::-1]
            res_caminho.append(original_destino)
            print(res_caminho)

        print("Caminhos disjuntos encontrados: %d " % max_caminhos_disjuntos)

        return max_caminhos_disjuntos