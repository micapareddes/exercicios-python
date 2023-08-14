list = [5, 2, 3, 1, 4, 12, 9, 0]
size = len(list)
for a in range(size):
    for i in range(size - 1):
        current = list[i]
        next = i + 1
        if current > list[next]:
            list[i] = list[next]
            list[next] = current


for item in list:
    if list[size - 1] == item:
        print(item)
    else: print(f'{item}', end = ',')
