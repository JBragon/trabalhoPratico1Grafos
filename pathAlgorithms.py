def bellman(Graph, origin):  # (grafo ponderado (Vertex, Edges, weight), vertice origem)
    # *** INICIALIZACAO ***
    dist = []
    pred = []

    for i in range(len(Graph)):
        # vetor que armazena a distancia de s a cada vertice
        dist.append(float('inf'))
        pred.append(None)  # vetor que armazena o predecessor de cada vertice

    dist[origin] = 0  # distancia ate o vertice origem eh 0
    # lista dos vertices a serem processados
    listOfVertex = [i for i in range(len(Graph))]

    # *** ALGORITMO ***
    for _ in range(len(listOfVertex)):  # percorre todos os vertices
        changed = False  # flag para controle do fluxo do programa

        # percorre novamente todos os vertices para verificacao de todas as arestas
        for i in range(len(listOfVertex)):
            index = 0

            if len(Graph[i]) > 0:
                for u in Graph[i][0]:
                    # se a distancia ate 'u' for maior que a distancia ate 'i' + peso da aresta
                    if dist[u] > dist[i] + Graph[i][1][index]:
                        # um novo caminho foi encontrado a partir de 'u'
                        dist[u] = dist[i] + Graph[i][1][index]
                        pred[u] = i  # coloca 'i' como predecessor de 'u'
                        changed = True  # aciona a flag para indicar que houve alteracoes
                    index += 1

        if not changed:  # se nao houve alteracoes nao eh necessario verificar as arestas novamente
            break

    return dist, pred

def dijkstra(Graph, origin):  # (grafo ponderado (Vertex, Edges, weight), vertice origem)
    # *** INICIALIZACAO ***
    distance = []
    pred = []

    for i in range(len(Graph)):
        # vetor que armazena a distancia de s a cada vertice
        distance.append(float('inf'))
        pred.append(None)  # vetor que armazena o predecessor de cada vertice

    distance[origin] = 0  # distancia ate o vertice origem eh 0
    # lista dos vertices a serem processados
    listOfVertex = [i for i in range(len(Graph))]

    # *** ALGORITMO ***
    while len(listOfVertex) != 0:  # enquanto existem vertices a serem processados, faca
        min = float('inf')  
        u = -1

        for i in listOfVertex:
            if distance[i] < min:  # condicao para pegar o vertice de menor distancia
                min = distance[i]  # pega a menor distancia ate 'i'
                u = i  # 'u' recebe o vertice de menor distancia

        if u == -1:  # condicao caso nao haja alteracao nas distancias
            break

        adjacentes = Graph[u]  # vertices adjacentes a 'u'
        # remove o vertice U dos vertices a serem processados
        listOfVertex.remove(u)
        indice = 0

        if len(adjacentes) > 0:  # se existem vertices adjacentes
            for v in adjacentes[0]:  # para cada vertice adjacente, faca
                # se a distancia ate V for maior que a distancia ate 'u' + peso da aresta
                if distance[v] > distance[u] + adjacentes[1][indice]:
                    # um novo caminho foi encontrado a partir de 'u'
                    distance[v] = distance[u] + adjacentes[1][indice]
                    pred[v] = u  # coloca 'u' como predecessor de 'v'
                indice += 1

    return distance, pred  # retorna os vetores de distancia e predecessor, respectivamente

def floyd(Graph):  # (grafo ponderado (Vertex, Edges, weight)
    # *** INICIALIZACAO ***
    dist = []
    pred = []

    for i in range(len(Graph)):
        pred.append([None for _ in range(len(Graph))])  # matriz de predecessores
        dist.append([float('inf')
                     for _ in range(len(Graph))])  # matriz de distancias

    for i in range(len(Graph)):  # para cada linha da matriz de dist e pred
        for j in range(len(Graph)):  # para cada coluna da matriz de dist e pred
            if i == j:  # se origem eh igual a destino
                dist[i][j] = 0  # distancia entre o mesmo vertice eh 0
            elif len(Graph[i]) > 0:  # se ainda existem arestas a serem analisadas
                if j in Graph[i][0]:  # caso exista aresta 'i' 'j'
                    index = list(Graph[i][0]).index(j)
                    # distancia recebe o peso da aresta
                    dist[i][j] = Graph[i][1][index]
                    pred[i][j] = i  # predecessor recebe o vertice 'i'
            else:  # nesse caso, nao se conhece o caminho 'i' 'j'
                dist[i][j] = float('inf')  # distancia, nesse caso, eh infinito
                pred[i][j] = None  # predecessor nulo

    # *** ALGORITMO ***
    for k in range(len(Graph)):  # procura caminhos alternativos passando por 'k'
        for i in range(len(Graph)):  # caminhos a partir de 'i'
            for j in range(len(Graph)):  # caminhos ate 'j'
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    # novo caminho, de 'i' a 'j', passando por 'k'
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]  # atualiza o predecessor

    return dist, pred
