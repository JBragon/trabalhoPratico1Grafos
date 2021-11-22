def bellman(Graph, origin):
    dist = []
    pred = []

    for i in range(len(Graph)):
        dist.append(float('inf'))
        pred.append(None)

    dist[origin] = 0
    listOfVertex = [i for i in range(len(Graph))]

    for _ in range(len(listOfVertex)):
        changed = False

        for i in range(len(listOfVertex)):
            index = 0

            if len(Graph[i]) > 0:
                for u in Graph[i][0]:
                    if dist[u] > dist[i] + Graph[i][1][index]:
                        dist[u] = dist[i] + Graph[i][1][index]
                        pred[u] = i
                        changed = True
                    index += 1

        if not changed:
            break

    return dist, pred

def dijkstra(Graph, origin):
    distance = []
    pred = []

    for i in range(len(Graph)):
        distance.append(float('inf'))
        pred.append(None)

    distance[origin] = 0
    listOfVertex = [i for i in range(len(Graph))]

    while len(listOfVertex) != 0:
        min = float('inf')  
        u = -1

        for i in listOfVertex:
            if distance[i] < min:
                min = distance[i]
                u = i

        if u == -1:
            break

        adjacent = Graph[u]
        listOfVertex.remove(u)
        index = 0

        if len(adjacent) > 0:
            for v in adjacent[0]:
                if distance[v] > distance[u] + adjacent[1][index]:
                    distance[v] = distance[u] + adjacent[1][index]
                    pred[v] = u
                index += 1

    return distance, pred

def floyd(Graph):
    dist = []
    pred = []

    for i in range(len(Graph)):
        pred.append([None for _ in range(len(Graph))])
        dist.append([float('inf')
                     for _ in range(len(Graph))])

    for i in range(len(Graph)):
        for j in range(len(Graph)):
            if i == j:
                dist[i][j] = 0
            elif len(Graph[i]) > 0:
                if j in Graph[i][0]:
                    index = list(Graph[i][0]).index(j)
                    dist[i][j] = Graph[i][1][index]
                    pred[i][j] = i
            else:
                dist[i][j] = float('inf')
                pred[i][j] = None

    for k in range(len(Graph)):
        for i in range(len(Graph)):
            for j in range(len(Graph)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred
