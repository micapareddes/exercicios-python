def factorial_of_number(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial

def calculate_number_of_combinations_in_set(n, p):
    if n < p:
        return "Erro: O número total de itens (n) não pode ser menor do que o número de itens que você está escolhendo (p)"
    else: 
        s = factorial_of_number(n) / (factorial_of_number(p) * factorial_of_number(n-p))
        return s

print(calculate_number_of_combinations_in_set(5, 3))