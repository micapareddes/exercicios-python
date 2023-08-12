# Creates matrix from user's input
def inputMatriz(qtLinhas):
    r = []
    for l in range(qtLinhas):
        r.append([int(ent) for ent in input().split()])
    return r

# Multiplies user's matrix by the row's respective number from the main diagonal
def matrix_times_main_diagonal(matrix):
    i = 0
    multiplied_matrix = []
    for row in matrix:
        multiplied_matrix.append([])
        for column in row:
            multiplied_matrix[i].append(column * matrix[i][i])
        i += 1
    return multiplied_matrix

# Gets input of lines
total_lines_matrix = int(input('Informe a quantidade de linhas que deseja na matriz: '))

# Gets the user's matrix
matrix = inputMatriz(total_lines_matrix)

# Gets the matrix multiplied by the diagonal
multiplied_matrix = matrix_times_main_diagonal(matrix)

# Separates the result from the user's input
print('-resultado----')

# Exibits new matrix without the '[]'
for row in multiplied_matrix:
    for col in row:
        print(f'{col} ', end = '')
    print()

