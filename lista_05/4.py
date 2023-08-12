temp = float(input('Por favor, informe o valor da temperatura que deseja converter: '))

unidade = input('Agora, selecione a unidade de medida (Celsius, Fahrenheit ou Kelvin): ')

celciusF = (temp - 32) / 1.8

celciusK = temp - 273

fahrK = (temp - 273) * 1.8 + 32

fahrC = temp * 1.8 + 32

kelC = temp + 273

kelF = (temp - 32) / 1.8 + 273

if unidade == 'Celsius' or unidade == 'celsius' or unidade == 'cel':
    print(f'Isso dá {fahrC}° garus Fahrenhite e {kelC}° graus Kelvin')

elif unidade == 'Fahrenheit' or unidade == 'fahrenhite' or unidade == 'fah':
    print(f'Isso dá {celciusF}° garus Celcius e {kelF}° graus Kelvin')

elif unidade == 'Kelvin' or unidade == 'kelvin' or unidade == 'kel':
    print(f'Isso dá {celciusK}° garus Celcius e {fahrK}° graus Kelvin')

else: print('Sinto muito, verifique se a unidade de medida foi escrita corretamente. Se não for alguma das 3 opções indicadas, não será possível realizar a conversão.')

''''
Correção pelo ChatGPT
-----------------------

temp = float(input('Por favor, informe o valor da temperatura que deseja converter: '))

unidade = input('Agora, selecione a unidade de medida (Celsius, Fahrenheit ou Kelvin): ').lower().strip()

if unidade not in ['celsius', 'c', 'cel', 'fahrenheit', 'f', 'fah', 'kelvin', 'k', 'kel']:

    print('Sinto muito, verifique se a unidade de medida foi escrita corretamente. Se não for alguma das 3 opções indicadas, não será possível realizar a conversão.')

else:
    if unidade in ['celsius', 'c', 'cel']:
        fahrC = temp * 1.8 + 32
    kelC = temp + 273
    print(f'Isso dá {fahrC:.2f}° Fahrenheit e {kelC:.2f}° Kelvin')
    
    elif unidade in ['fahrenheit', 'f', 'fah']:
    celciusF = (temp - 32) / 1.8
    kelF = (temp - 32) / 1.8 + 273
    print(f'Isso dá {celciusF:.2f}° Celsius e {kelF:.2f}° Kelvin')
    
    elif unidade in ['kelvin', 'k', 'kel']:
    celciusK = temp - 273
    fahrK = (temp - 273) * 1.8 + 32
    print(f'Isso dá {celciusK:.2f}° Celsius e {fahrK:.2f}° Fahrenheit')

'''