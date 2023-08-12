entrada = float(input('Insira qualquer número: '))

calculo = entrada % 2

if calculo > 0: 
    print(f'O número {entrada} não é par')

else: print('O número informado é par')