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

list = [1, 2, 3, 4, 5]
print(sum_even_nums_on_list(list))
