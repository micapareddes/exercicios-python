import sys
sys.path.append("/Users/micaela/Documents/Python_Elder")
from funcoes.mica_funcoes import is_prime_num

def prime_num_on_list(num_list):
    primes_list = []
    index = 0

    while index < len(num_list):
        number = num_list[index]
        
        if is_prime_num(number):
            primes_list.append(number)

        index += 1
    return primes_list

num_list = [100, 101, 11, 3, 79709, 23648, 30, 0, 1]

print(prime_num_on_list(num_list))

