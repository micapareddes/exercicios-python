numero_entrada = int(input('Digite um número inteiro no intervalo de 1 a 9: '))

if numero_entrada == 0:
        print('Programa encerrado.')

else:
    while numero_entrada < 1 or numero_entrada > 9:
        print('O número informado deve ser menor do que 9 e maior do que 1.')
        numero_entrada = int(input('Digite um número inteiro no intervalo de 1 a 9: '))
    
    numero_divisivel = 1
    contador = 0

    while numero_divisivel <= 1000:
        validar_divisibilidade = numero_divisivel % numero_entrada

        if validar_divisibilidade == 0:
           contador += 1

        numero_divisivel = numero_divisivel + 1
        
    print(f'O número {numero_entrada} é divisor de {contador} números no intervalo de 1 a 1000.')