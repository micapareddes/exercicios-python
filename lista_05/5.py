print('Bem-vindo ao criador de triângulos. Aqui te informo a categoria do triângulo de acordo com o tamanho dos seus lados.')

lado1 = float(input('Insira o tamanho do primeiro lado: '))

lado2 = float(input('Insira o tamanho do segundo lado: '))

lado3 = float(input('Insira o tamanho do terceiro lado: '))

condicao1 = lado1 < lado2 + lado3

condicao2 = lado2 < lado1 + lado3

condicao3 = lado3 < lado1 + lado2

condicao4 = lado1 > abs(lado2 - lado3)

condicao5 = lado2 > abs(lado1 - lado3)

condicao6 = lado3 > abs(lado1 - lado2)

condicaoExistencia = condicao1 and condicao2 and condicao3 and condicao4 and condicao5 and condicao6

equi = lado1 == lado2 == lado3

iso1 = lado1 == lado2
iso2 = lado2 == lado3
iso3 = lado3 == lado1

if lado1 < 0 or lado2 < 0 or lado3 < 0: 
    print('Os valores precisam ser positivos. Por favor, tente novamente.')

elif condicaoExistencia == False:
    print('Um triângulo com esses valores não pode existir :(')

elif equi: print('Esses valores formam um Triângulo Eqüilátero')

elif iso1 or iso2 or iso3: print('Esses valores formam um Triângulo Isósceles')

else: print('Esses valores formam um Triângulo Escaleno')

''''
Correção pelo ChatGPT
-----------------------
print('Bem-vindo [...]')

lado1 = float(input('Insira o tamanho do primeiro lado: '))
lado2 = float(input('Insira o tamanho do segundo lado: '))
lado3 = float(input('Insira o tamanho do terceiro lado: '))

if lado1 < 0 or lado2 < 0 or lado3 < 0: 
    print('Os valores precisam ser positivos. Por favor, tente novamente.')
elif lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2:
    print('Um triângulo com esses valores não pode existir :(')
else:
    if lado1 == lado2 == lado3:
        print('Esses valores formam um Triângulo Equilátero')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('Esses valores formam um Triângulo Isósceles')
    else:
        print('Esses valores formam um Triângulo Escaleno')

'''