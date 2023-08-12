def define_matrix_of_zero(row, column):
    matrix = []
    for i in range(row):
        matrix.append([])
        for j in range(column):
            matrix[i].append(0)
        
    for row in matrix:
        print(row)

row = int(input('Defina o total de linhas: '))
column = int(input('Defina o total de colunas: '))

define_matrix_of_zero(row, column)