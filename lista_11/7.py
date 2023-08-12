#informa True or False para matriz quadrada

#exemplo:

# # #                             # # #
# # #            # # #            #
# # #  <-- True  # # # <-- False  # #

'''''

1. Se: len(matrix[0]) == len(matrix):
    # verificar se há alguma outra lista de tamanho diferente
        - se sim: False
        - se não há: True

2. Se outra coisa:
    False

'''

def square_matrix(matrix):
    if len(matrix[0]) == len(matrix):
        for list in matrix:
            if len(list) != len(matrix):
                return False
        return True
    return False
    
matrix = [
    [1, 1, 1],
    [1, 1, 2],
    [1, 2, 3],
    []
]

print(square_matrix(matrix))
