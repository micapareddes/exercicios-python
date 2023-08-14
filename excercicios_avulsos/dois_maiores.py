def inputListaInteiros():
    return [int(ent) for ent in input().split()]

num_list =  inputListaInteiros()
list_length = len(num_list)

if list_length < 1:
    print('A lista deve conter pelo menos um número')

else:
    largest_num = num_list[0]
    second_largest_num = num_list[0]

    if list_length == 1:
        print(f'{largest_num} nenhum')
    
    else:
        index = 0
        
        while index < list_length:

            if largest_num < num_list[index]:
                if largest_num > second_largest_num:
                    second_largest_num = largest_num
                largest_num = num_list[index]
                
            elif largest_num == second_largest_num:
                second_largest_num = num_list[index]
            
            elif second_largest_num < num_list[index]:
                second_largest_num = num_list[index]      
            index += 1

        print(f'{largest_num} {second_largest_num}')