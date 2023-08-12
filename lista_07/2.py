total_numbers = int(input('Quantos números você deseja informar? '))

while total_numbers <= 0:
    print('Você deve informar um número maior do que zero.')
    total_numbers = int(input('Quantos números você deseja informar?'))

counter_input_number = 0
factorials_sum = 0

while total_numbers > counter_input_number:

    input_number = int(input('Digite o número: '))
    counter_factorial = 1
    equal_input_number = input_number
    controle = input_number

    while counter_factorial < controle:
        input_number -= 1
        equal_input_number *=input_number
        counter_factorial += 1


    factorials_sum += equal_input_number
    counter_input_number += 1

print(f'A soma do fatorial dos números informados é: {factorials_sum}')


'''
Correção - ChatGPT:
-----------------------
A única coisa que vou fazer é refatorar um pouco para facilitar a leitura, renomear algumas variáveis para inglês e remover algumas linhas desnecessárias. Aqui está a versão refatorada:
------------------------
num_values = int(input('Quantos números você deseja informar? '))

while num_values <= 0:
    print('Você deve informar um número maior do que zero.')
    num_values = int(input('Quantos números você deseja informar?'))

num_counter = 0
sum_factorials = 0

while num_values > num_counter:
    current_value = int(input('Digite o número: '))
    factorial_value = 1
    counter_factorial = 1

    while counter_factorial <= current_value:
        factorial_value *= counter_factorial
        counter_factorial += 1

    sum_factorials += factorial_value
    num_counter += 1

print(f'A soma do fatorial dos números informados é: {sum_factorials}')

'''
