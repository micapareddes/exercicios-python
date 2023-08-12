print('Para calcular a área do trapezio, precisarei de algumas informações.')

entrada1 = input('Primeiro, digite a altura do trapezio:')

entrada2 = input('Agora, me diga qual o tamanho da base superior (a menor): ')

entrada3 = input('Por último, qual o tamanho da base inferior (a maior): ')

altura = float(entrada1)

basePeq = float(entrada2)

baseMaior = float(entrada3)

areaTrapezio = ( altura * (basePeq + baseMaior) ) / 2

print(f'A área do trapezio, de acordo às informações fornecidas, é: {areaTrapezio:.1f}')