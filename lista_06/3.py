num = int(input('Escreva um número qualquér: '))

multiplicador = 1

while multiplicador <= 10:
    resultado = num * multiplicador
    print(f'{num} x {multiplicador} = {resultado}')
    multiplicador += 1