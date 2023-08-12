numeroEntrada = int(input('Insira algum número: '))

if numeroEntrada < 0:
    print('Sinto muito, mas o número deve ser maior do que zero.')

else:
    numero = 1
    multiplicador = 1
    while numero < numeroEntrada:
        numero = numero + 1
        multiplicador = numero * multiplicador
print(f'O resultado do produtorio do 1 até o número {numeroEntrada} é: {multiplicador}')
