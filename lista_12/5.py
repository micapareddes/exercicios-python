def find_zero_diagonals(sm):
    size = len(sm)
    above = []
    below = []

    for a in range(size - 1):
        position = 1
        for b in range(1, size):
            if a != b and sm[a][b] == 0 and position not in above:
                above.append(position)
            
            if a != b and sm[b][a] == 0 and position not in below:
                below.append(position)
            position += 1
            
    print('As seguintes diagonais possuem zero:')
    
    for position in above:
        print(f'{position} diagonal acima da principal')

    for position in below:
        print(f'{position} diagonal abaixo da principal')


# Testing code
m = [
    [1, 0, 2],
    [0, 2, 0],
    [0, 0, 3]
]

find_zero_diagonals(m)