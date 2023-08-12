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

print(bigger_num([]))