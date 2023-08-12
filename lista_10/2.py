def transform_to_absolute_value(num_list):

    if len(num_list) <= 0:
        return 'Error: A lista deve conter pelo menos um número'

    index = 0
    absolute_value_num_list = []

    while index < len(num_list):

        number = num_list[index]

        if number < 0:

            absolute_value_num_list.append(number * -1)

        else: absolute_value_num_list.append(number)

        index += 1
    
    return absolute_value_num_list

num_list = [-3]

print(transform_to_absolute_value(num_list))

'''''
ChatGPT 
- Nessa versão, eu reordenei as linhas de código para que fiquem mais agrupadas por sua funcionalidade. Além disso, usei uma expressão condicional (também conhecida como ternário) para calcular o valor absoluto, o que torna o código mais conciso.

def transform_to_absolute_value(num_list):
    if len(num_list) <= 0:
        return 'Error: A lista deve conter pelo menos um número'

    absolute_value_num_list = []
    index = 0

    while index < len(num_list):
        number = num_list[index]
        absolute_value = -number if number < 0 else number #ternário
        absolute_value_num_list.append(absolute_value)
        index += 1
    
    return absolute_value_num_list

num_list = [-3]
print(transform_to_absolute_value(num_list))

'''