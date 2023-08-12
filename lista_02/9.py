nome = input('Digite seu nome: ')

print(f'Olá {nome}, hoje irei lhe ajudar a cacular o desconto do produto da sua escolha!')

valor = float(input('Primeiro, me diga qual o preço do produto? R$'))

desconto = float(input('Agora, me diga qual a porcentagem de desconto? '))

novoValor = valor - ( valor * (desconto / 100) )

print(f'O valor desse produto após sofrer um desconto de {desconto:.0f}% será de R${novoValor:.2f}')