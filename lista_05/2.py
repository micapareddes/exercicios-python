valor1 = float(input('Por favor, insira um número qualquer: '))

valor2 = float(input('Por favor, insira outro número qualquer: '))

if valor1 == valor2:
    print('Sinto muito, mas os números devem ser diferentes entre sí.')

elif valor1 > valor2:
    print(f'{valor1} é o maior número, enquanto {valor2} é o menor. ')

elif valor2 > valor1:
    print(f'{valor2} é o maior número, enquanto {valor1} é o menor. ')
