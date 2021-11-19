# (lista de predecessores, vertice origem, vertice destino)
def writeTraveledPathWithFloyd(pred, origem, destino):
    caminho = [destino]  # caminho inicializa com o vertice destino
    s = destino

    while s != origem:  # enquanto o vertice destino for diferente do vertice origem
        if pred[origem][s] is None:  # se nao existe um predecessor
            return []  # retorna uma lista vazia

        # se o predecessor existe, este eh adicionado a 's'
        s = pred[origem][s]
        # insere 's' na primeira posicao da lista de caminho
        caminho.insert(0, s)

    return caminho  # retorna o caminho


# (lista de predecessores, vertice origem, vertice destino)
def writeTraveledPath(pred, origem, destino):
    caminho = [destino]  # caminho inicializa com o vertice destino
    s = destino

    while s != origem:  # se vertice destino eh diferente do vertice origem
        if pred[destino] is None:  # se nao existe predecessor para o vertice destino
            return []  # retorna uma lista vazia

        s = pred[s]  # 's' recebe o predecessor de 's'
        # insere 's' na primeira posicao da lista de caminho
        caminho.insert(0, s)

    return caminho  # retorna o caminho
