import os

# função responsável em ler o arquivo de grafos e estruturar 
# da forma convencional para a execução dos algoritmos de percurso
#formado 0 vertice origem - [(Arestas), (Pesos das arestas)]
def readFile(fileName):
    file = []

    with open(os.path.dirname(os.path.realpath(__file__)) +  "\\Datasets\\"+fileName, 'r', encoding='utf-8') as toy:
        for line in toy:
            stripped_line = line.strip()
            lineList = stripped_line.split()
            file.append(lineList)

    numberOfVertex=int(file[0][0])

    #limando a primeira posição com o número de vértices e arestas
    file.pop(0)

    Graph = [] #grafo que será retornado

    for i in range(numberOfVertex):  #para cada vertice, adiciona uma posição no grafo
        Graph.append([[],[]])
        
    for i in range(len(file)):

        vertex, adjacency, weight = file[i]

        # liga o vertex aleatorio 'adjacencia' ao vertice 'randomVertex'
        Graph[int(vertex)][0].append(int(adjacency))
        
        # adiciona o peso dessa aresta
        Graph[int(vertex)][1].append(int(weight))
        
    for i in range(len(Graph)):  # percorre o grafo
        if len(Graph[i]) > 0:  # se existe arestas para o vertice 'i'
            Graph[i][0] = tuple(Graph[i][0])  # tupla que representa as arestas
            # tupla que representa, respectivamente, os pesos das arestas
            Graph[i][1] = tuple(Graph[i][1])

    return Graph, numberOfVertex
