def two_list(list_a, list_b):
    new_list = []
    index = 0
    while index < len(list_a) and index < len(list_b):
        num_a = list_a[index]
        num_b = list_b[index]
        new_list.append(num_a * num_b)
        index += 1    

    if len(list_a) > len(list_b):
        while index < len(list_a):
            num_a = list_a[index]
            new_list.append(num_a)
            index += 1

    
    elif len(list_b) > len(list_a):
        while index < len(list_b):
            num_b = list_b[index]
            new_list.append(num_b)
            index += 1

    return new_list

a = [1, 0]
b = [0]

print(two_list(a, b))