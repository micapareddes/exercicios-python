#divide numeros de uma lista pelo maior num presente nela e retorna uma nova lista com o resultado da divisão
def divide_numbers_by_largest_num(num_list):
    largest_num = max(num_list)
    new_list = []
    index = 0

    while index < len(num_list):
        number = num_list[index]
        new_list.append( ( number / largest_num ) )
        index += 1

    return new_list


num_list = [1, 0]

print(divide_numbers_by_largest_num(num_list))