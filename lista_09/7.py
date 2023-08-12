from math import factorial

def factorial_of_nums_on_list(num_list):
    len_list = len(num_list)
    ind = 0

    while ind < len_list:
        num = num_list[ind]
        print(f'Factorial do número {num}: {factorial(num)}')
        ind += 1

lista = [2, 3, 4, 5]
factorial_of_nums_on_list(lista)