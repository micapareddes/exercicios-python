nome = input('Oi, eu sou o Idade-Teller! Me diga, qual é o seu nome? ')

print(f'Prazer, {nome}!')

anoNac = float(input('Agora, me conta, em qual ano você nasceu? '))

anoAtual = float(input('Antes de adivinhar a sua idade, preciso que me de uma ajuda! Em que ano estamos atualmente? '))

idade = anoAtual - anoNac

print(f'Você tem {idade:.0f} anos! Entretanto, se ainda não chegou seu aniversário, você fará {idade:.0f} anos ainda este ano! Parabéns!')

