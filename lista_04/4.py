entrada = input('Insira uma letra: ')

a = entrada == 'a'

e = entrada == 'e'

i = entrada == 'i'

o = entrada == 'o'

u = entrada == 'u'

if a or  e or i or o or u: 
    print(f'A letra {entrada} é uma vogal.')

else: print(f'A letra {entrada} não é uma vogal.')