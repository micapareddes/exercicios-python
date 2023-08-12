entrada1 = input('Digite o valor de a: ')

entrada2 = input('Digite o valor de x: ')

a = float(entrada1)

x = float(entrada2)

funcaoDerivada = a * ( x ** (a - 1))

print(f'O valor da função derivada é: {funcaoDerivada:.0f}')
