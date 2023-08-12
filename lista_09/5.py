def is_num_on_list(num_list, num):
    ind = 0
    len_list = len(num_list)
    while ind < len_list:
        num_verify = num_list[ind]
        if num == num_verify:
            return True
        ind += 1
    return False

print(is_num_on_list([1, 2, 3], 4))
