def is_prime_num(num):
    divider_of_num = 1
    total_dividers = 1
    while divider_of_num < num:
        divider_of_num = divider_of_num + 1
        if num % divider_of_num == 0:
            total_dividers = total_dividers + 1
    if total_dividers == 2:
        return True
    return False
    
def next_prime_num(num):
    num +=1
    while is_prime_num(num) is not True:
        num +=1
    return num

user_num = int(input('Digite um número inteiro maior ou igual à 0: '))
next_prime_of_user_num = next_prime_num(user_num)
print(f'O próximo primo ao número informado é {next_prime_of_user_num}.')

''''
ChatGPT 
-----------------------
def is_prime_num(num):
    if num <= 1:
        return False
    divider_of_num = 2
    while divider_of_num < num:
        if num % divider_of_num == 0:
            return False 
        divider_of_num += 1
    return True

def next_prime_num(num):
    num += 1
    while is_prime_num(num) is not True:
        num += 1
    return num

user_num = int(input())
next_prime_of_user_num = next_prime_num(user_num)
print(next_prime_of_user_num)

'''