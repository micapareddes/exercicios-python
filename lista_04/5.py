num1 = int(input('Digite um número :'))

num2 = int(input('Digite outro número :'))

calculo = num1 % num2

if calculo == 0: 
    print(f'O número {num1} é múltiplo do número {num2}')

else: print(f'O número {num1} não é múltiplo do número {num2}')