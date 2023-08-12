num1 = float(input('Insira qualquer número: '))

num2 = float(input('Insira outro número: '))

num3 = float(input('Insira outro número, novamente: '))

condicao1 = num1 != num2

condicao2 = num1 != num3

condicao3 = num2 != num3

if condicao1 and condicao2 and condicao3: 
    print('Todos os números são diferentes')

else: print('Você inseriu alguns números iguais')