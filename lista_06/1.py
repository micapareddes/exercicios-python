entrada = int(input('Insira algum número: '))

if entrada < 1: 
    print('O número deve ser maior do que 1. Por favor, tente novamente.')

else:
    num = 1
    while num <= entrada:
        print(f'{num}')
        num = num + 2

''''
Correçao ChatGPT
-----------------
entrada = int(input('Insira algum número: '))

if entrada < 1: 
    print('O número deve ser maior que 1 para ver os números ímpares.')

else:
    num = 1
    while num <= entrada:
        print(f'{num}')
        num += 2 <-- melhora a legibilidade

'''