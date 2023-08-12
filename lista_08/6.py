def factorial_of_number(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial

def approximate_euler_number(number_of_terms):
    if number_of_terms <= 0:
        return 
    
    else:
        counter = 1
        e = 1 / factorial_of_number(counter)
        while counter < number_of_terms:
            e += 1/factorial_of_number(counter)
            counter += 1
            
        return e
    

print(approximate_euler_number(5))


'''''
ChatGPT:

Não há necessidade de ter um bloco else após o if de retorno. Isso ocorre porque se a condição if for atendida, a função retornará e terminará, então tudo o que vem depois do if já será como em um bloco else.
Aqui está a versão revisada do seu código:

def factorial_of_number(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial

def approximate_euler_number(number_of_terms):
    if number_of_terms <= 0:
        return 

    counter = 1
    e = 1 / factorial_of_number(0)
    while counter < number_of_terms:
        e += 1/factorial_of_number(counter)
        counter += 1

    return "{:.{}f}".format(e, number_of_terms) #garante que o resultado tenha o mesmo número de casas decimais que number_of_terms, mesmo que as últimas casas sejam zeros.

print(approximate_euler_number(5))

'''