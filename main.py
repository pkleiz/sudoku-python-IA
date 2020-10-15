# programa para criar um tabuleiro completo de sudoku
# resolvendo sudoku usando hillclimbing
# CopyRight Pedro Kleiz e Gabriel Luna V3.0
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀ ⠈⢻⣿⣿⡄⠀
# ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀ ⠀⠀⠈⠙⢿⣷⡄⠀
# ⠀⠀⣀⣤⣴⣶⣿⡟⠀ ⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀ ⠀⠀ ⠀⠀⠀⠀⣿⣷⠀
# ⠀⢰⣿⡟⠋⠉⣹⣿ ⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
# ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
# ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
# ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢸⣿⣧⠀
# ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢸⣿⣿⠀⠀ ⠀
#  ⣿⣿⠀⠀⠀⣿⣿⡇⠀                    ⢸⣿⣿⠀⠀
# ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇
# ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⣿⣿⠃
# ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀ ⢸⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀ ⠀⣸⣿⠇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⠁ ⠈⠻⣿⣿⣿⣿⡿⠏⠀
# ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀
# ------------------------------------------------------------

from random import *
from numpy import *
from itertools import *

# funcao principal que inicia o programa e chama os metodos subsequentes


def sudoku():
  solucao = geraSolucaoAleatoria()
  pontuacaoSolucao = avaliaSolucao(solucao)

  #Informações estatisticas
  contadorDeRodadas = 0
  reinicio = pontuacaoSolucao
  contadorDeReinicio = 0
  novosTabuleirosGerados = 0

  somaDeScoreInicial = pontuacaoSolucao
  mediaDeScoreInicial = 0

  somaDeScoreTrocaDeTabuleiro = 0
  mediaDeScoreTrocaDeTabuleiro = 0

  mediaDeScorePorGeracao = 0
  while True:
    contadorDeRodadas += 1
    
    if pontuacaoSolucao == 0:
        break
    
    novaSolucao = solucao
    aceitaSolucaoMelhor(novaSolucao)

    pontuacao = avaliaSolucao(novaSolucao)

    if avaliaSolucao(novaSolucao) < pontuacaoSolucao:
        solucao = novaSolucao
        pontuacaoSolucao = pontuacao

    #Verifica se ele reiniciou com um novo tabuleiro
    if(pontuacaoSolucao == reinicio):
        contadorDeReinicio+=1
    else:
        print("Score: ", pontuacaoSolucao,"\n          Solucao ")
        for i in range(9):
            print(solucao[i],"\n")
        print("Rodada Atual: ", contadorDeRodadas, "\n")
        print("Quantidade de novos tabuleiros Gerados: ", novosTabuleirosGerados, "\n\n \n")
        print("Media de Score Inicial dos Tabuleiros: ", round(mediaDeScoreInicial,2), "\n\n \n")
        print("Media de Score na troca de tabuleiro: ", round(mediaDeScoreTrocaDeTabuleiro,2), "\n\n \n")
        print("Media de melhoria de Score antes da troca de tabuleiro: ", round(mediaDeScorePorGeracao,2), "\n\n \n")
        reinicio = pontuacaoSolucao
        contadorDeReinicio = 0
    #gera um novo tabuleiro se a solucao nao convergir para um score melhor
    if(contadorDeReinicio >= 500):
        mediaDeScorePorGeracao = mediaDeScoreInicial - mediaDeScoreTrocaDeTabuleiro
        somaDeScoreTrocaDeTabuleiro = pontuacaoSolucao + somaDeScoreTrocaDeTabuleiro
        mediaDeScoreTrocaDeTabuleiro = somaDeScoreTrocaDeTabuleiro / novosTabuleirosGerados
        solucao = geraSolucaoAleatoria()
        pontuacaoSolucao = avaliaSolucao(solucao)
        novosTabuleirosGerados+=1
        somaDeScoreInicial = pontuacaoSolucao + somaDeScoreInicial
        mediaDeScoreInicial = somaDeScoreInicial/novosTabuleirosGerados
        
        
#----------------=======------- Step 1 Gerar Solucao --------------------------------------
            
# gera solucao aleatoria onde as constantes nao se modificam
def geraSolucaoAleatoria():
    tabuleiro = []
    # criando tabuleiro previamente preenchido
    for i in range(1, 10):
        linha = []
        for j in range(1, 10):
            if(i == 1 and j == 4):
                linha.append(7)
            elif(i == 2 and j == 1):
                linha.append(1)
            elif(i == 3 and j == 4):
                linha.append(4)
            elif(i == 3 and j == 5):
                linha.append(3)
            elif(i == 3 and j == 7):
                linha.append(2)
            elif(i == 4 and j == 9):
                linha.append(6)
            elif(i == 5 and j == 4):
                linha.append(5)
            elif(i == 5 and j == 6):
                linha.append(9)
            elif(i == 6 and j == 7):
                linha.append(4)
            elif(i == 6 and j == 8):
                linha.append(1)
            elif(i == 6 and j == 9):
                linha.append(8)
            elif(i == 7 and j == 5):
                linha.append(8)
            elif(i == 7 and j == 6):
                linha.append(1)
            elif(i == 8 and j == 3):
                linha.append(2)
            elif(i == 8 and j == 8):
                linha.append(5)
            elif(i == 9 and j == 2):
                linha.append(4)
            elif(i == 9 and j == 7):
                linha.append(3)
            else:
                linha.append(randint(1, 9))
        tabuleiro.append(linha)
    return tabuleiro

# ----------------------------- Step 2 Avalia Solucao -----------------------------------

# metodo que avalia o atual sudoku
def avaliaSolucao(solucao):

    contaRepetidosLinha = contaRepetidos(solucao)
    #transposição da matriz para pegar os valores da coluna
    contaRepetidosColuna = ((array(solucao)).transpose())
    contaRepetidosColuna = contaRepetidos(contaRepetidosColuna.tolist())
    contaRepetidosBloco = contaBloco(solucao)


    return contaRepetidosLinha + contaRepetidosColuna + contaRepetidosBloco
# objetivo a ser alcancado

# Conta o numero de ocorrencias repetidas linha a linha
def contaRepetidos(matrizContar):
  somaTotal = 0

  #separa linha a linha e conta o numero de repetidos
  for i in range(len(matrizContar[0])):
    #defino um dicionario vazio onde vou adicionando os valores dos indices
    contaRepetidosLinha = {}

    #Adiciona ao dicionario criado
    for item in matrizContar[i]:
      contaRepetidosLinha[item] = matrizContar[i].count(item)
    
    #cria o interador para ser varrido no tamanho da linha da matriz e converte para lista
    tamanhoRepetidos = len(contaRepetidosLinha)
    listaDosValores = list(contaRepetidosLinha.values())

    #verifico quantas vezes ele esta se repetindo para criar o valor final da funcao
    for valor in range(tamanhoRepetidos):
      if (listaDosValores[valor] > 1):
        somaTotal = somaTotal + listaDosValores[valor] - 1
    return somaTotal

#separa a matriz 9x9 em 9 blocos 3x3 e faz a soma de cada um deles
def contaBloco(matriz):

    blocosSomados = []
    #separa em 9 blocos
    bloco1 = [matriz[0][0:3], matriz[1][0:3], matriz[2][0:3]]
    bloco2 = [matriz[0][3:6], matriz[1][3:6], matriz[2][3:6]]
    bloco3 = [matriz[0][6:9], matriz[1][6:9], matriz[2][6:9]]
    bloco4 = [matriz[3][0:3], matriz[4][0:3], matriz[5][0:3]]
    bloco5 = [matriz[3][3:6], matriz[4][3:6], matriz[5][3:6]]
    bloco6 = [matriz[3][6:9], matriz[4][6:9], matriz[5][6:9]]
    bloco7 = [matriz[6][0:3], matriz[7][0:3], matriz[8][0:3]]
    bloco8 = [matriz[6][3:6], matriz[7][3:6], matriz[8][3:6]]
    bloco9 = [matriz[6][6:9], matriz[7][6:9], matriz[8][6:9]]


    #faz a soma de cada repetição nos blocos e adiciona a lista
    blocosSomados.append(somaBloco(bloco1))
    blocosSomados.append(somaBloco(bloco2))
    blocosSomados.append(somaBloco(bloco3))
    blocosSomados.append(somaBloco(bloco4))
    blocosSomados.append(somaBloco(bloco5))
    blocosSomados.append(somaBloco(bloco6))
    blocosSomados.append(somaBloco(bloco7))
    blocosSomados.append(somaBloco(bloco8))
    blocosSomados.append(somaBloco(bloco9))

    return (sum(blocosSomados))

#Calcula a soma dos blocos um a um depois de corver-los em lista
def somaBloco(lista):
  somaTotal = 0
  listaContar= list(chain(*lista))
  #separa linha a linha e conta o numero de repetidos

  contaRepetidosLinha = {}

  #Adiciona ao dicionario criado
  for item in listaContar:
    contaRepetidosLinha[item] = listaContar.count(item)

  tamanhoRepetidos = len(contaRepetidosLinha)
  listaDosValores = list(contaRepetidosLinha.values())

  #verifico quantas vezes ele esta se repetindo para criar o valor final da funcao
  for valor in range(tamanhoRepetidos):
    if (listaDosValores[valor] > 1):
      somaTotal = somaTotal + listaDosValores[valor] - 1
  return somaTotal

# sao os indices que nao podem ser mudados ao rodar a funcao
# de melhor solucao
def retornaIndicesConstantes():
    indices = [(0, 3), (1, 0), (2, 3), (2, 4), (2, 6), (3, 8),
               (4, 3), (4, 5), (5, 6), (5, 7), (5, 8), (6, 4),
               (6, 5), (7, 2), (7, 7), (8, 1), (8, 6)]
    return indices

# vai para um estado aleatorio e modifica para um
# valor aleatorio (nao sendo esse uma constante)

#-------------------------- Step 3 Aceitar modificações --------------------------------

def aceitaSolucaoMelhor(solucao):
    indicesConstantes = retornaIndicesConstantes()
    i = randint(0, 8)
    j = randint(0, 8)

    if(((i, j) not in indicesConstantes)):
        solucao[i][j] = randint(1, 9)
    else:
        while True:
            i = randint(0, 8)
            j = randint(0, 8)

            if(((i, j) not in indicesConstantes)):
                solucao[i][j] = randint(1, 9)
                break

#--------------------------- Outros (ignorar) ------------------------------------------
sudokuPerfeito= [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]