print('Bem-vindo ao criador de triângulos. Aqui te respondo se o triângulo que vc deseja seria matemáticamente possível existir. Para isso, preciso que me diga os valores dos 3 lados do mesmo.')

lado1 = float(input('Insira o tamanho do primeiro lado: '))

lado2 = float(input('Insira o tamanho do segundo lado: '))

lado3 = float(input('Insira o tamanho do terceiro lado: '))

condicao1 = lado1 < lado2 + lado3

condicao2 = lado2 < lado1 + lado3

condicao3 = lado3 < lado1 + lado2

condicao4 = lado1 > abs(lado2 - lado3)

condicao5 = lado2 > abs(lado1 - lado3)

condicao6 = lado3 > abs(lado1 - lado2)

if lado1 < 0 or lado2 < 0 or lado3 < 0: 
    print('Os valores precisam ser positivos. Por favor, tente novamente.')

elif condicao1 and condicao2 and condicao3 and condicao4 and condicao5 and condicao6: 
    print(f'Um triângulo com os valores: {lado1}, {lado2} e {lado3} pode existir! :)')

else: print('Um triângulo com esses valores não pode existir :(')