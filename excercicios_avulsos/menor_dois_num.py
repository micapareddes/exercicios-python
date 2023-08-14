first_num = float( input() )
second_num = float( input() )

a = first_num
b = second_num

if a < b:
    print(f'O menor número é {a}')

elif b < a:
    print(f'O menor número é {b}')

else:
    print('Ambos números são iguais')