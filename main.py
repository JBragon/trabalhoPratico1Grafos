from writePath import writeTraveledPathWithFloyd, writeTraveledPath
from time import time
from pathAlgorithms import dijkstra, bellman, floyd
from importFile import readFile
import os

while True:

    print("\nArquivos:\n")

    filesList = os.listdir(os.path.dirname(os.path.realpath(__file__)) +  "\\Datasets\\")

    for file in filesList:
        print(filesList.index(file), "-", file)
        
    fileIndex = int(input("\nSelecione um grafo: "))
   
    if fileIndex+1 > len(filesList) or fileIndex < 0:
        print("Arquivo inexistente!")
        break

    os.system('cls||clear')
    
    fileName = filesList[fileIndex]

    graph, lastVertex = readFile(fileName)

    for i in range(len(graph)):
        print(str(i), "- ", str(graph[i]))

    print("\n")

    origin = int(input(f"Origem (de 0 a {lastVertex - 1}):"))

    if origin < 0 or origin > lastVertex-1:
        print("Origem invalida!")
        break

    destiny = int(input(f"Destino (de 0 a {lastVertex - 1}):"))

    if destiny < 0 or destiny > lastVertex-1:
        print("Destino invalido!")
        break

    os.system('cls||clear')
    print("Escolha um algoritmo para percorrer o grafo:")

    option = int(input("1- Dijkstra\n2- Bellman-Ford\n3- Floyd-Warshall\n-1 - para sair\n-> "))
    print("\n")

    starTime = time()

    print("Processando...")


    if option == 1:

        dist, pred = dijkstra(graph, origin)
        
        os.system('cls||clear')

        print("Caminho:", writeTraveledPath(pred, origin, destiny))
        print(f"Custo: {dist[destiny]}")

        endTime = time()
        print(f"Tempo de execução: {endTime - starTime}")

    if option == 2:

        dist, pred = bellman(graph, origin)

        os.system('cls||clear')

        print("\nCaminho:", writeTraveledPath(pred, origin, destiny))
        print(f"Custo: {dist[destiny]}")

        endTime = time()
        print(f"Tempo de execução: {endTime - starTime}")

    if option == 3:
        dist, pred = floyd(graph)

        os.system('cls||clear')

        print("\nCaminho:", writeTraveledPathWithFloyd(pred, origin, destiny))
        print(f"Custo: {dist[origin][destiny]}")

        endTime = time()
        print(f"Tempo de execução: {endTime - starTime}")

    if option < 0 or option > 3:
        break

    input("Pressione enter para continuar...")
    os.system('cls||clear')
