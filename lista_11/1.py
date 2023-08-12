#funcao

#recebe matriz numerica

#retorna somatorio de todos os elementos

def sum_matrix(matrix):
    equal = 0

    for line in matrix:
        for element in line:
            equal += element

    return equal

matrix = [
    [2, 2],
    [3, 4],
    [5, 6, 7, 0]
]

print(sum_matrix(matrix))