"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduandos em Sistemas de Informação
IF969 - Algoritmos e Estrutura de Dados

Autor: Daniel Freire Turmina (dft)
Email: dft@cin.ufpe.br
Autor: Yuri Correia de Barros (ycb)
Email: ycb@cin.ufpe.br

Data: 31-10-2020

Copyright(c) 2020 Daniel Freire Turmina & Yuri Correia de Barros
"""

vertices = {}
   
def insereVertice(num): 
    if num not in vertices:
        vertices[num] = [[], False, None, float('inf')] 

def insereAresta(origem,destino,peso): 
    if origem in vertices and destino in vertices:
        if destino not in vertices[origem][0]:
          vertices[origem][0].append([destino, peso])
    
def estacao(nome): 
    nomeMaiusc = str(nome)
    try:
        return dicVertices[nomeMaiusc.upper()]
    except:
        None

def dijkstra(vInicial, destino):
    if vInicial in vertices:
        vertices[vInicial][3] = 0
        atual = vInicial
        noVisitados = []

        caminho = []
        partida = destino 

        tamanho =  len(dicVertices)
        for a in range(1,tamanho+1):
            noVisitados.append(a)
        
        while len(noVisitados) > 0:
            for adj in vertices[atual][0]:
                if vertices[adj[0]][1] == False:
                    if vertices[atual][3] + adj[1] < vertices[adj[0]][3]:
                        vertices[adj[0]][3] = vertices[atual][3] + adj[1]
                        vertices[adj[0]][2] = atual
            
            vertices[atual][1] = True
            noVisitados.remove(atual)
        
            if len(noVisitados) > 0:
                pesoAtual = vertices[noVisitados[0]][3]
                verticeMinimo = noVisitados[0]
                for x in noVisitados:
                    if pesoAtual > vertices[x][3]:
                        pesoAtual = vertices[x][3]
                        verticeMinimo = x

            atual = verticeMinimo     

    while partida != None:
        caminho.insert(0, partida)
        partida = vertices[partida][2]
    return [caminho, vertices[destino][3]]                   
 

diretorio = "BaseDados-MetroToquio.txt" 

dataBase = open(diretorio, 'r')  
leArq = dataBase.read()
linhas = leArq.split('\n')
dicVertices = {}
dicVerticesInvertido = {}
n = 1
for quebra in linhas:
    listaInicial = quebra.split(",")
    vertice = str(listaInicial[0].upper()) 
    teste = vertice in dicVertices
    if teste == False:
        dicVertices[vertice] = n
        dicVerticesInvertido[n] = vertice 
        n += 1

tamanho =  len(dicVertices)

for a in range(1,tamanho+1):
      insereVertice(a)

for i in linhas:
    vetorLinha = i.split(',') 
    estacaoInicial = estacao(vetorLinha[0]) 
    estacaoFinal = estacao(vetorLinha[1][1:])
    dist = int(float(vetorLinha[2])*1000) 
    insereAresta(estacaoInicial, estacaoFinal, dist)

dataBase.close() 

estacaoStr1 = input('Digite o nome da Estação de Partida: ')
estacaoStr2 = input('Digite o nome da Estação de Destino: ')
estacaoNum1 = estacao(estacaoStr1)
estacaoNum2 = estacao(estacaoStr2)
print("\n=-=-=-=-=-=-=-=-==-=-=")

if estacaoNum1 != None and estacaoNum2 != None:
    print("\nA Rota mais Curta é:\n")
    caminhoPercorrido = dijkstra(estacaoNum1, estacaoNum2) 
    for i in caminhoPercorrido[0]:
        print(dicVerticesInvertido[i]) 

    print("\nCom uma distância de: ")
    print(int(caminhoPercorrido[1])/1000, 'Km')
    
elif estacaoNum1 == None and estacaoNum2 == None:
    print("\nA estação ", estacaoStr1, " e a estação ", estacaoStr2, " não existem nesta rede!")

elif estacaoNum1 == None:
    print('\nA Estação "', estacaoStr1, '" não existe!')

elif estacaoNum2 == None:
    print('\nA Estação "', estacaoStr2, '" não existe!')
