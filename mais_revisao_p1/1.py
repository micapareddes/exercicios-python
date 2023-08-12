def next_odd_num(num):
    return (2 * num) - 1

user_input = int(input())

counter = 1
counter_line = 0
number_to_print = 1
print(number_to_print)

while counter < user_input:

    counter += 1

    while counter_line < next_odd_num(counter):

        print(f'{number_to_print}', end = '')

        number_to_print += 1
        counter_line += 1

    counter_line = 0
    number_to_print = 1

    print()
    
counter = user_input - 1
    
while counter > 0:

    while counter_line < next_odd_num(counter):

        print(f'{number_to_print}', end = '')

        number_to_print += 1
        counter_line += 1

    counter_line = 0
    number_to_print = 1

    print()
    
    counter -= 1