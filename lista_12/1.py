'''''
FUNÇÃO
-------
* assuma que a matriz inserida sempre é quadrada
--------
Recebe matriz e retorna a média dos elementos da diagonal principal
1. percorrer elementos da diagonal e somar numa variável
2. dividir essa soma pelo tamanho da matriz
3. retornar valor

00 01 02
10 11 12 --> diagonal principal = 00 11 22 
20 21 22
'''

def average_of_main_diagonal(square_matrix):
    size = len(square_matrix)
    sum = 0

    for i in range(size):
        sum += square_matrix[i][i]

    avarage = sum / size

    return avarage

m = [
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8]
    ]

print(average_of_main_diagonal(m))