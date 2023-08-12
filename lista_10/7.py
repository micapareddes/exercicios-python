def exchange_positions_even_list(original_list):
    
    len_original_list = len(original_list)
    even_num = len_original_list % 2 == 0
    

    if not even_num or len_original_list == 0:
        return 'Error: Lista deve ser ter um total de elementos par e ser maior do que zero.'
    
    else:
        exchange_list = []
        exchange_list += original_list
        index = 0
        
        while index < len_original_list:
            exchange_list[len(original_list) - index - 1] = original_list[index]
            index += 1
        return exchange_list
    
lista = []

print(exchange_positions_even_list(lista))