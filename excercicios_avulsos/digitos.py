number = int(input())
result = number // 10
count = 1

if number < 0:
    while result < -1:
        number = result
        result = number // 10
        count += 1

else: 
    while result > 0:
        number = result
        result = number // 10
        count += 1

print(count)