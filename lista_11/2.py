#funcao

#recebe matriz

#retorna quadro com cada linha e elemento de cada linha, separado por espaco (linha x coluna)

#exemplo:
    # # # 
    # # # 
    # # #

def line_and_column(matrix):
    for line in matrix:
        for col in line:
            print(f'{col} ', end = '')
        print()
    return '<3'
    
matrix = [
    [1, 2, 1],
    [2, 3, 2],
    [3, 4, 3],
    [4, 5, 4]
]

print(line_and_column(matrix))