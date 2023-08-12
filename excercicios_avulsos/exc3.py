first_num = float( input() )
second_num = float( input() )
third_num = float( input() )

a = first_num
b = second_num
c = third_num

if a > b and a > c:
    print(f'O maior número é {a}')

elif b > a and b > c:
    print(f'O maior número é {b}')

elif c > a and c > b:
    print(f'O maior número é {c}')

else:
    print('Todos os números informados são iguais')