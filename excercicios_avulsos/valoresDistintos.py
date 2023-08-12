input_number = int(input())
all_numbers = []

while input_number != -1:
    all_numbers.append(input_number)
    input_number = int(input())

current_index = 0
repeated_numbers = []
distinct_numbers = []

while current_index < len(all_numbers):
    
    current_number = all_numbers[current_index]
    next_index = current_index + 1
    
    if current_number not in repeated_numbers:
        
        while next_index < len(all_numbers):
            
            next_number = all_numbers[next_index]
            
            if current_number == next_number:
                repeated_numbers.append(current_number)
                break
            
            elif next_index == len(all_numbers) - 1:
                distinct_numbers.append(current_number)
            
            next_index += 1
            
        if current_index == len(all_numbers) - 1:
            distinct_numbers.append(current_number)
        
    current_index += 1

print(len(distinct_numbers), distinct_numbers)

""""
num = int(input())
num_list = []

while num != -1:
    num_list.append(num)
    num = int(input())
        
 
index_current = 0
same_num = []
dif_num = []

while index_current < len(num_list):
    
    current = num_list[index_current]
    index_next = index_current + 1
    
    if current not in same_num:
        
        while index_next < len(num_list):
            
            next_num = num_list[index_next]
            
            if current == next_num:
                same_num.append(current)
                break
            
            elif index_next == len(num_list) - 1:
                dif_num.append(current)
            
            index_next += 1
            
        if index_current == len(num_list) - 1:
            dif_num.append(current)
        
        
    index_current += 1

'''''
index_current = 0
while index_current < len(num_list):
    current = num_list[index_current]
    if current not in same_num:
        dif_num.append(current)
    index_current += 1
'''   

print(len(dif_num), dif_num)
"""  