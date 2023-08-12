def factorial_of_number(num):
    factorial = num
    while num > 1:
        num -= 1
        factorial *= num

    return factorial


print(factorial_of_number(0))

'''''
ChatGPT:

Seu código está quase correto, mas note que se a função for chamada com o número 0, ela retornará 0, quando deveria retornar 1 (pois o fatorial de 0 é definido como 1).
Aqui está a versão corrigida:

def factorial_of_number(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1

    return factorial

print(factorial_of_number(5))  # Deve retornar 120


'''