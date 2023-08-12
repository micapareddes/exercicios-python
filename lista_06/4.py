num1 = int(input('Informe um número inteiro:'))

num2 = int(input('Informe um número inteiro maior ao anterior:'))

if num1 > num2:
    print(f'O número {num2} deve ser maior ao número {num1}')

else:
    bloco = num1
    soma = num1
    while  bloco < num2:
        #print(f'bloco: {bloco}')
        bloco += 1
        #print(f'soma: {soma}')
        soma += bloco
    print(f'O resultado da somatoria é: {soma}')


    #somatoria = soma do intervalo
        #ex. 1 e 6
        # 1 + 2 + 3 + 4 + 5 + 6

''''
Clean Code 
------------
    - nomes claros
    - espaço ao redor dos operadores (+=)
--------------------------------------------

limite_inferior = int(input('Informe um número inteiro como limite inferior: '))
limite_superior = int(input('Informe um número inteiro maior que o anterior como limite superior: '))

if limite_inferior > limite_superior:
    print(f'O número {limite_superior} deve ser maior ao número {limite_inferior}')
else:
    numero_atual = limite_inferior
    soma = limite_inferior
    while numero_atual < limite_superior:
        numero_atual += 1
        soma += numero_atual
    print(f'O resultado da somatoria é: {soma}')

'''