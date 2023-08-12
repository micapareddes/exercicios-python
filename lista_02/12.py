nome = input('Digite seu nome: ')

print(f'Olá {nome}! Hoje irei lhe ajudar a calcurar qual o valor total a ser pago no alugel do carro')

km = float(input('Por favor, digite os kilometros percorridos com o carro alugado, em kilometros: '))

dias = float(input('Agora, informe o total de dias pelos quais o carro fora alugado: '))

valor = (0.15 * km) + (60 * dias)

print(f'O valor total a ser pago pelo aluguel do carro é R${valor}')