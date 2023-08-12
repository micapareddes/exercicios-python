'''''
FUNÇÃO
-------
* assuma que a matriz inserida sempre é quadrada
--------
1. percorrer elementos da diagonal secundaria
2. compara elemento atual com 1 elemento da diagonal sec
3. se todos forem iguais retorna True
4. se tiver algum numero diferente retorna False


00 01 02
10 11 12 --> diagonal secundaria = 02 11 20 -> 0 1 2 / 2 1 0
20 21 22
'''

def is_sec_diagonal_equal(square_matrix):
    size = len(square_matrix)
    first_element_of_diagonal = square_matrix[0][size - 1]

    for i in range(size):
        current_element = square_matrix[i][(size - 1) - i]

        if current_element != first_element_of_diagonal:
            return False
    
    return True

m = [
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8]
    ]

print(is_sec_diagonal_equal(m))
