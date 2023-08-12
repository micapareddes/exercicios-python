import sys
sys.path.append('/Users/micaela/Documents/Python_Elder')
from funcoes.mica_funcoes import is_regular_matrix

def is_square_matrix(matrix): # era para importar porém nunca foi feito em exc.
    dimension_matrix = is_regular_matrix(matrix)

    if not dimension_matrix:
        return False
    
    row_matrix = dimension_matrix[0]
    column_matrix = dimension_matrix[1]

    if row_matrix != column_matrix:
        return False

    return True


def extract_max_row_min_column(matrix):
    square_matrix = is_square_matrix(matrix)
    if not square_matrix:
        return 'Error: matrix must be square'
    
    size = len(matrix)
    max_row = []
    min_col = []

    for a in range(size):
        bigger_num = matrix[a][0]
        small_num = matrix[0][a]
        for b in range(size):
            if matrix[a][b] > bigger_num:
                bigger_num = matrix[a][b]
            
            if matrix[b][a] < small_num:
                small_num = matrix[b][a]
        
        max_row.append(bigger_num), min_col.append(small_num)

    return [max_row, min_col]

m = [
    [0, 1, 2],
    [3, 4, 5], 
    [6, 7, 0]
]

print(extract_max_row_min_column(m))