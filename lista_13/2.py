"""""
FUNÇÃO
--------
1. recebe qntd de linhas (row) e colunas
2. recebe um limite (int)
3. retorna matriz de dimensões - linhas e colunas
4. elementos da matriz são produzidos aleatoriamente a partir do limite (-lim a +lim)

---------
matrix = []
random = 0 #num entre -limite e +limite
def funcao(row, col, lim):
    for i in range(row):
        matrix.append([])
        for j in range(col):
            matrix[i].append(random)
    return matrix

    for row in matrix:
        print(row)

"""
from random import randint

def create_random_matrix(row, col, lim):
    matrix = []
    for i in range(row):
        matrix.append([])
        for j in range(col):
            random = randint(-lim, lim)
            matrix[i].append(random)
    return matrix

row = int(input('Definha o total de linhas: '))
col = int(input('Defina o total de colunas: '))
lim = int(input('Defina o limite: '))

matrix = create_random_matrix(row, col, lim)

for row in matrix:
    print(row)