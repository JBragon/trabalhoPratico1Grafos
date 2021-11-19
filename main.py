from writePath import writeTraveledPathWithFloyd, writeTraveledPath
from time import time
from pathAlgorithms import dijkstra, bellman, floyd
from importFile import readFile
import os

loop = 0

while True:  # loop do menu

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

    #imprime a estrutura do grafo
    for i in range(len(graph)):
        print(str(i), "- ", str(graph[i]))

    print("\n")

    origin = int(input("Escolha o vértice origem: "))

    if origin < 0 or origin > lastVertex-1:
        print("Vertice de origem invalido!")
        break

    destiny = int(input("Escolha o vértice destino: "))

    if destiny < 0 or destiny > lastVertex-1:
        print("Vertice de destino invalido!")
        break

    os.system('cls||clear')
    print("Escolha um algoritmo para percorrer o grafo:")

    option = int(input("1- Dijkstra\n2- Bellman-Ford\n3- Floyd-Warshall\n-1 - para sair\n-> "))
    print("\n")

    starTime = time()  # para calcular o tempo de execução

    print("Processando o algoritmo. Aguarde...")

    # algoritmo de dijkstra
    if option == 1:
        # executa o algoritmo de dijkstra
        dist, pred = dijkstra(graph, origin)
        
        os.system('cls||clear')

        # impressao, na tela, dos dados
        print(f"Custo: {dist[destiny]}")
        print("Caminho percorrido: ", writeTraveledPath(pred, origin, destiny))

        endTime = time()  # para calcular o tempo de execucao
        print(f"Tempo de execução: {endTime - starTime}")

    # algoritmo de bellman-ford
    if option == 2:
        # executa o algoritmo de bellman-ford
        dist, pred = bellman(graph, origin)

        os.system('cls||clear')

        # impressao, na tela, dos dados
        print(f"Custo: {dist[destiny]} unidades")
        print("Caminho mínimo: ", writeTraveledPath(pred, origin, destiny))

        endTime = time()
        print(f"Tempo de execução: {endTime - starTime}")

    # algoritmo de floyd-warshall
    if option == 3:
        # executa o algoritmo de floyd-warshall
        dist, pred = floyd(graph)

        os.system('cls||clear')

        # impressao, na tela, dos dados
        print("\nCaminho mínimo: ", writeTraveledPathWithFloyd(pred, origin, destiny))
        print(f"Custo: {dist[origin][destiny]} unidades")

        endTime = time()
        print(f"Tempo de execução: {endTime - starTime}")

    # condicao para sair do loop
    if option < 0 or option > 3:
        break

    input("Pressione enter para continuar...")
    os.system('cls||clear')

    loop += 1
