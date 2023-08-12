# recebe matriz com textos

# retorna qual linha e coluna com texto vazio (nulo)


# <-- linha   # # # # <-- coluna
#             
#
#

'''''
1. definir a funcao que recebe matriz

2. percorre linha por linha e item por item de cada linnha e verifica se há uma string vazia
    - se há: guarda index da linha e index da coluna
    - se nao há: continua percorrendo

linha = matrix[index]
coluna = matrix[index][index]

3. retorna index guardados, modificados +1

'''

def null_string(matrix):
    count_line = 0
    len_matrix = len(matrix)
    index_line = 0
    found_null = False

    while count_line < len_matrix:
        count_col = 0
        index_col = 0
        line = matrix[index_line]
        len_line = len(line)

        while count_col < len_line:
            column = matrix[index_line][index_col]
            if column == '':
                print(f'Linha: {index_line + 1}, coluna: {index_col + 1}')
                found_null = True #chatGPT: para retornar mensagem caso nao haja null
            index_col += 1
            count_col += 1

        index_line += 1
        count_line += 1

    if found_null is False:
        print('Não foram encontradas strings vazias na matriz.')

matrix = [
    ['OI', 'OIIII', ''],
    ['O9', 'O8', ''],
    ['Null', 'None', '']
]
null_string(matrix)