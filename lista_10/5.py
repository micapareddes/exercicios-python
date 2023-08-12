import sys
sys.path.append("/Users/micaela/Documents/Python_Elder")
from funcoes.mica_funcoes import next_prime_num
from funcoes.mica_funcoes import is_prime_num

def list_of_next_primes_numbers(number_of_primes, starting_num):
    
    primes_list = []
    number = starting_num
    index = 0

    while index < number_of_primes:
        prime_num = next_prime_num(number)
        
        primes_list.append(prime_num)

        number = prime_num
        
        index += 1
    return primes_list

print(list_of_next_primes_numbers(10, 1))