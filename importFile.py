import os

def readFile(fileName):
    file = []

    with open(os.path.dirname(os.path.realpath(__file__)) +  "\\Datasets\\"+fileName, 'r', encoding='utf-8') as toy:
        for line in toy:
            stripped_line = line.strip()
            lineList = stripped_line.split()
            file.append(lineList)

    numberOfVertex=int(file[0][0])

    file.pop(0)

    Graph = []

    for i in range(numberOfVertex):
        Graph.append([[],[]])
        
    for i in range(len(file)):

        vertex, adjacency, weight = file[i]

        Graph[int(vertex)][0].append(int(adjacency))
        
        Graph[int(vertex)][1].append(int(weight))
        
    for i in range(len(Graph)):
        if len(Graph[i]) > 0:
            Graph[i][0] = tuple(Graph[i][0])
            Graph[i][1] = tuple(Graph[i][1])

    return Graph, numberOfVertex
