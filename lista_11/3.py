#recebe matriz de textos

#retorna maior texto da matriz

def bigger_string(matrix):

    previous_element = len('')

    for line in matrix:
        for element in line:
            if len(element) > previous_element:
                previous_element = len(element)
                bigger_string = element

    return(bigger_string)

matrix = [ 
    ['te amo', 'jo'],
    ['te amo', 'jony'],
    ['te amo mais do que tudo', 'jonathan']
]

print(bigger_string(matrix))