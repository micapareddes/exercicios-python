entrada1 = input('Digite o valor do primeiro cateto: ')

entrada2 = input('Digite o valor do segundo cateto: ')

cat1 = int(entrada1)

cat2 = int(entrada2)

hip = ((cat1 ** 2) + (cat2 ** 2)) ** (1 / 2)

print(f'O valor da hipotenusa, de acordo com os valores de cateto fornecidos, é: {hip}')