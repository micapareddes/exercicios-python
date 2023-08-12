line_total = int(input('Informe uma quantidade total de linhas: '))

while line_total <= 0:
    print('O número informado não pode ser menor do que zero.')
    line_total = int(input('Informe uma quantidade total de linhas: '))


actual_line = '*'
line_counter = 1

while line_total >= line_counter:
    print(f'{actual_line}')
    line_counter += 1
    actual_line += ' *'


''''
Correção ChatGPT:
-----------------
total_lines = int(input('Informe uma quantidade total de linhas: '))

while total_lines <= 0:
    print('O número informado não pode ser menor do que zero.')
    total_lines = int(input('Informe uma quantidade total de linhas: '))

current_line = 1

while total_lines >= current_line:
    print('* ' * current_line)
    current_line += 1

------------------------
Nessa linha, estamos multiplicando a string "* " pelo número da linha atual (current_line), o que efetivamente imprime o número correto de estrelas para cada linha. Isso ocorre porque, em Python, a multiplicação de uma string por um número resulta na string sendo repetida aquele número de vezes.
----------------------------
'''