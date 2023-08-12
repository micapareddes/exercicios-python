nome = input('Digite seu nome: ')

print(f'Olá {nome}, sou o conversor de temperatura! Hoje irei lhe ajudar a converter sua temperatura de Celsius a Fahrenheit. Bora lá :)')

celcius = float(input('Me diga, qual a temperatura em Celcius que deseja converter? '))

fahrenheit = ( (9 * celcius) / 5 ) + 32

print(f'{celcius:.0f}º graus Celcius em Fahrenheit é {fahrenheit:.0f}º')