entrada = float( input('insira um número de tres digitos ou mais: ') )

ver1 = entrada / 100

ver2 = (entrada % 100) //10

ver3 = (ver2 - 1) % 2 

if ver1 >= 1:
    if ver3 == 0: print(f'O penúltimo dígito do número {entrada} é ímpar')
    else: print(f'O penúltimo dígito do número {entrada} é par')

else:
    print('O número inserido tem menos de 3 dígitos, por favor, tente novamente.')

