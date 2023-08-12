def is_regular_matrix(matrix):
    if not matrix:
        return []
    
    first_row_size = len(matrix[0])

    for row in matrix:
        if len(row) != first_row_size:
            return []
    return [len(matrix), first_row_size]

def multiply_matrix_except_diagonal(matrix):
    math_matrix = is_regular_matrix(matrix)
    rows_matrix = math_matrix[0]
    columns_matrix = math_matrix[1]

    if not math_matrix:
        return 'Error: a matriz deve ser matemática'
    
    result_matrix =  []
    for i in range(rows_matrix):
        result_matrix.append([])
        for j in range(columns_matrix):
            if i == j:
                result_matrix[i].append(0)
            else:
                result_matrix[i].append(matrix[i][j] * 10)

    return result_matrix

# Test
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(multiply_matrix_except_diagonal(m))

# expected output: 
'''''
[
    [0, 20, 30],
    [40, 0, 60],
    [70, 80, 0]
]
'''
