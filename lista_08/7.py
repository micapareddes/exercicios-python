def factorial_of_number(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial

def approximate_cos(total_number_of_terms, x):
    if 0 > x or x > 1:
        return 
    
    counter = 2
    cos = 1 - ((x ** counter) / factorial_of_number(counter))

    while counter < total_number_of_terms * 2:
        counter += 2
        cos += (x ** counter) / factorial_of_number(counter)
        counter += 2
        cos -= (x ** counter) / factorial_of_number(counter)
        
    return cos

print(approximate_cos(5,1))

'''''
ChatGPT

def factorial_of_number(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial

def approximate_cos(total_number_of_terms, x):
    if 0 > x or x > 1:
        return 
    
    counter = 0
    cos = 1 
    sign = -1

    while counter < total_number_of_terms:
        counter += 1
        cos += sign * ((x ** (2 * counter)) / factorial_of_number(2 * counter))
        sign *= -1  # Inverte o sinal para o próximo termo

    return cos

print(approximate_cos(3, 1))

'''