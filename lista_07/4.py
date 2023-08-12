input_lines = int(input('Informe uma quantidade total de linhas: '))

while input_lines <= 0:
    print('O número informado não pode ser menor do que zero.')
    input_lines = int(input('Informe uma quantidade total de linhas: '))

total_lines = (input_lines * 2) - 1 
actual_line = '* '
line_counter = 1

while input_lines >= line_counter: 
    while input_lines >= line_counter:
            print(actual_line * line_counter)
            line_counter += 1
            
    new_line_counter = input_lines
    while new_line_counter > 1:
         new_line_counter -= 1
         print(actual_line * new_line_counter)

''''
Correção ChatGPT:
-----------------
input_lines = int(input('Informe uma quantidade total de linhas: '))

while input_lines <= 0:
    print('O número informado não pode ser menor do que zero.')
    input_lines = int(input('Informe uma quantidade total de linhas: '))

current_line = 1

# print the top half of the diamond (including the middle line)
while input_lines >= current_line:
    print('* ' * current_line)
    current_line += 1

# print the bottom half of the diamond (excluding the middle line)
current_line = input_lines - 1
while current_line >= 1:
    print('* ' * current_line)
    current_line -= 1

'''

