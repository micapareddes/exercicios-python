""""Verifica se o número inserido é primo. Retorna: True caso seja primo e False caso não seja."""
def is_prime_num(num):
    if num <= 1:
        return False
    divider_of_num = 2
    while divider_of_num < num:
        if num % divider_of_num == 0:
            return False 
        divider_of_num += 1
    return True

""""Retorna o próximo primo do numero informado"""
def next_prime_num(num):
    num += 1
    while is_prime_num(num) is not True:
        num += 1
    return num

""""Retorna o maior número da lista"""
def bigger_num(list):
    if not list:
        return 'Error: lista não pode ser vazia'
    list_len = len(list)
    ind = 0
    bigger_num = list[0]
    while ind < list_len:
        num = list[ind]
        if num > bigger_num:
            bigger_num = num
        ind += 1
    return bigger_num

""""Retorna a quantidade de números primos que a lista possui"""
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

""""Inverte a ordem da lista (esta função nao tem retorno)"""
def invert_list_order(list):
    list_len = len(list)
    ind = list_len - 1

    while ind >= 0:
        print (list[ind])
        ind -= 1

""""Soma apenas os números primos de uma lista de números"""
def sum_even_nums_on_list(list):
    list_len = len(list)
    ind_list = 0
    even_num = []
    even_num_sum = 0

    while ind_list < list_len:
        list_num = list[ind_list]
        if list_num % 2 == 0:
            even_num_sum += list_num
            even_num.append(list_num)
        ind_list += 1

    return even_num_sum

""""Verifica se um número se encontra na lista"""
def is_num_on_list(num_list, num):
    ind = 0
    len_list = len(num_list)
    while ind < len_list:
        num_verify = num_list[ind]
        if num == num_verify:
            return True
        ind += 1
    return False

""""Faz as somatórias de duas listas e retorna um valor lógico se a primeira lista é maior que a segunda"""
def is_sum_of_first_list_bigger(first_list, sec_list):
    return first_list > sec_list

""""Faz o factorial de cada numero na lista"""
from math import factorial

def factorial_of_nums_on_list(num_list):
    len_list = len(num_list)
    ind = 0

    while ind < len_list:
        num = num_list[ind]
        print(f'Factorial do número {num}: {factorial(num)}')
        ind += 1
    
""""Calcula a media e moda de uma llista de notas de 0 a 10"""
from statistics import mean
from statistics import mode

def median_and_mode_of_grades(grades_list):
    ind = 0
    len_list = len(grades_list)
    while ind < len_list:
        grade = grades_list[ind]
        if grade < 0 or grade > 10:
            return None
        ind += 1

    moda = mode(grades_list)
    media = mean(grades_list)

    return [media, moda]

""""Verifica se palavra é um palindromo"""
def is_it_a_palindrome(word):
    ind = len(word) - 1
    reversed_word = []
    word_list =[]
    ind_word = 0

    while ind_word < len(word):
        word_list.append(word[ind_word])
        ind_word += 1

    while ind >= 0:
        letter = word[ind]
        reversed_word.append(letter)
        ind -= 1
    return reversed_word == word_list

""""Verifica se possui mesmo tamanho de colunas"""
def is_regular_matrix(matrix):
    if not matrix: # ChatGPT: Verifica se a matriz está vazia
        return []
    
    first_row_size = len(matrix[0])

    for row in matrix:
        if len(row) != first_row_size:
            return []
    return [len(matrix), first_row_size]
""""Verifica se a matriz é quadrada"""
