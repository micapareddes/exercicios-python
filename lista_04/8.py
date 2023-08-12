entrada = float(input('Bem-vindo à caixa automática, informe o valor do saque que deseja realizar: R$'))

calculo = entrada % 5

nota50 = entrada // 50
sobra50 = entrada % 50

nota10 = sobra50 // 10
sobra10 = sobra50 % 10

nota5 = sobra10 // 5
sobra5 = sobra10 % 5

if calculo != 0:
    print('Sinto-muito, não temos a quantidade de cédulas disponíveis para realizar o saque. Por favor, dirija-se a outro caixa.')

elif sobra50 == 0: 
    print(f'Você receberá {nota50:.0f} cédula(s) de R$50. Obrigada pela preferência!')

elif sobra50 > 0 and sobra10 == 0 : 
    print(f'Você receberá {nota50:.0f} cédula(s) de R$50 e {nota10:.0f} cédula(s) de R$10. Obrigada pela preferência!')

elif sobra50 > 0 and sobra10 > 0:
    print(f'Você receberá {nota50:.0f} cédula(s) de R$50, {nota10:.0f} cédula(s) de R$10 e {nota5:.0f} cédula(s) de R$5. Obrigada pela preferência!')