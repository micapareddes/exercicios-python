entrada = int(input('Informe um número inteiro: '))

if entrada == 0: 
    print('Programa encerrado.')

else: 
    contador = 1
    soma = entrada

    while entrada > 0:
        entrada = int(input('Informe um número inteiro: '))
        if entrada > 0:
            contador = contador + 1
            soma = soma + entrada

    media = soma / contador
    print(f'Você digitou um total de {contador} números, a soma deles é igual a {soma} e a média é {media}')

