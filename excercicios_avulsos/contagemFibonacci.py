input_number = int(input())
all_numbers = []

while input_number >= 0:
    all_numbers.append(input_number)
    input_number = int(input())

index = 0
lenght_all_numbers = len(all_numbers)
counter = 0

while index < lenght_all_numbers:
    
    current_input_number = all_numbers[index]
    current_input_number_is_first_three_fibonacci_digits = current_input_number == 0 or current_input_number == 1

    if current_input_number_is_first_three_fibonacci_digits:
        counter += 1
        bigger_number = current_input_number

    else:
        current_fibonacci_number = 2
        first_fibonacci = 1
        second_fibonacci = 2

        while current_input_number >= current_fibonacci_number:

            if current_input_number == current_fibonacci_number:
                counter += 1
                bigger_number = current_input_number
            
            current_fibonacci_number = first_fibonacci + second_fibonacci
            first_fibonacci = second_fibonacci
            second_fibonacci = current_fibonacci_number

    index += 1

print(counter, bigger_number)
'''''
input_number = int(input())
all_numbers = []

while input_number >= 0:
    all_numbers.append(input_number)
    input_number = int(input())

index = 0
lenght_all_numbers = len(all_numbers)
counter = 0

while index < lenght_all_numbers:
    
    current_input_number = all_numbers[index]
    current_input_number_is_first_three_fibonacci_digits = current_input_number == 0 or current_input_number == 1

    if current_input_number_is_first_three_fibonacci_digits:
        counter += 1
        bigger_number = current_input_number

    else:
        current_fibonacci_number = 2
        first_fibonacci = 1
        second_fibonacci = 2

        while current_input_number >= current_fibonacci_number:

            if current_input_number == current_fibonacci_number:
                counter += 1
                bigger_number = current_input_number
            
            current_fibonacci_number = first_fibonacci + second_fibonacci
            first_fibonacci = second_fibonacci
            second_fibonacci = current_fibonacci_number

    index += 1

print(counter, bigger_number)
'''