def multiply_by_main_diagonal(sm):
    size = len(sm)
    multiplied_matrix = []

    for i in range(size):
        multiplied_matrix.append([])
        for j in range(size):
            multiplied_matrix[i].append(sm[i][i] * sm[i][j])
    return multiplied_matrix
    
m = [
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3]
    ]

print(multiply_by_main_diagonal(m))