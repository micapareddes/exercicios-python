import sys
sys.path.append("/Users/micaela/Documents/Python_Elder")
from funcoes.mica_funcoes import is_prime_num

def prime_num_on_list(list):
    ind = 0
    list_len = len(list)
    counter_of_primes = 0

    while ind < list_len:
        num = list[ind]
        if is_prime_num(num):
            counter_of_primes += 1
        ind += 1

    return (f'A lista possui {counter_of_primes} números primos.')

list = [2, 3, 5, 7]

print(prime_num_on_list(list))