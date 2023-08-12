print('Olá, sou o assistente da Aviação 5.5 e hoje irei lhe ajudar a verificar se você cumpre os requisitos para ingressar ao nosso curso de aviação. Para isso, irei precisar algumas informações:')

altura = float(input('Digite, em metros, sua altura (por favor, utilize ponto ao invez de virgula): '))

idade = int(input('Agora, digite sua idade: '))

horas = int(input('Me diga, quantas horas de voô completadas você possui? '))

peso = float(input('Quantos kilos você pesa? '))

conAltura = altura >= 1.75

condIdade = 40 >= idade >= 22

conVoo = horas >= 1600

conPeso = 95 >= peso >= 65

if conAltura and condIdade and conVoo and conPeso: 
    print('Parabéns! Você cumpre todos os requisitos e poderá ingressar ao nosso curso! Até lá!')

else: print('Sinto muito, você não cumpre os requisitos necessários para ingressar no nosso curso de aviação :(')