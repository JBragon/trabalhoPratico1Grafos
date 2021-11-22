
def writeTraveledPathWithFloyd(pred, origem, destino):
    caminho = [destino]
    s = destino

    while s != origem:
        if pred[origem][s] is None:
            return []

        s = pred[origem][s]
        caminho.insert(0, s)

    return caminho

def writeTraveledPath(pred, origem, destino):
    caminho = [destino]
    s = destino

    while s != origem:
        if pred[destino] is None:
            return []

        s = pred[s]
        caminho.insert(0, s)

    return caminho
