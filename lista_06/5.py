multiplo = int(input('Insira um número o qual deseja ver seus múltiplos: '))

total_multiplos = int(input('Insira o total de múltiplos que deseja ver: '))

print(f'Aqui os {total_multiplos} múltiplos de {multiplo}:')
numNatural = 0
while numNatural <= total_multiplos:
    resultado = multiplo * numNatural
    print(f'{resultado}')
    numNatural += 1