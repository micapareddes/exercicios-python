#entrada = float(print('Insira um número: '))
entrada = float(input('Insira qualquer número: '))


calculo = entrada % 2

if entrada >= 0:
    if calculo == 0: print(f'O número {entrada:.0f} é par')
    else: print(f'O número {entrada} é ímpar')

else: print('O número precisa ser positivo.')