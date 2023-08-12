'''''
FUNÇAO
-------
1. recebe uma matriz
2. se a matriz possui colunas de diferentes tamanhos 
    retorna lista vazia []
    ex. matriz = [
    [0, 0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
    ]
3. caso contrario, retorna lista com qntde rows e qntde col
    ex. matriz = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
    ]

    retorna = [3, 3]

def row_col_matrix(matrix):
    if len(matrix) == len(matrix[0]):
        for row in matrix:
            act_col = 0
            for column in row:
                act_col += 1
            size_columns.append(col)
            if act_col not in size_columns:
                return []
        return [len(matrix), act_col]
    else: 
        return []

size_columns = []
def row_col_matrix(matrix):
    for row in matrix:
        size_columns.append(len(row))
        if len(row) != size_columns[0]:
            return []
    return [len(matrix), len(row)]

'''


def is_regular_matrix(matrix):
    if not matrix: # ChatGPT: Verifica se a matriz está vazia
        return []
    
    first_row_size = len(matrix[0])

    for row in matrix:
        if len(row) != first_row_size:
            return []
    return [len(matrix), first_row_size]


    
m = [
]
print(is_regular_matrix(m))