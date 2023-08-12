def is_regular_matrix(matrix):
    if not matrix:
        return []
    
    first_row_size = len(matrix[0])

    for row in matrix:
        if len(row) != first_row_size:
            return []
    return [len(matrix), first_row_size]

# feito pelo chatGPT:
def sum_matrices(matrix1, matrix2):
    dimensions_matrix1 = is_regular_matrix(matrix1)
    dimensions_matrix2 = is_regular_matrix(matrix2)

    if not dimensions_matrix1 or not dimensions_matrix2:
        return False

    if dimensions_matrix1 != dimensions_matrix2:
        return False

    result_matrix = []
    for i in range(dimensions_matrix1[0]): # i começa sempre valendo 0 e vai aumentando até o valor do range (range = [0, 1, 2, ...])
        row_sum = []
        for j in range(dimensions_matrix1[1]):
            row_sum.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(row_sum)

    return result_matrix

# Test
matrix_a = [
    [1, 2],
    [3, 4],
    [3, 3]
]

matrix_b = [
    [5, 6],
    [7, 8],
    [3, 3]
]

print(sum_matrices(matrix_a, matrix_b))
