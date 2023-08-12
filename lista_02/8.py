nome = input('Digite seu nome: ')

print(f'Olá {nome}, hoje irei lhe ajudar a cacular seu novo salário após o aumento.')

salarioAtual = float(input('Me diga, qual é o seu salário atual? R$'))

aumento = float(input('Agora, me diga qual a porcentagem do aumento: %'))

salarioAumentado = salarioAtual * (aumento / 100)

novoSalario = salarioAtual + salarioAumentado

print(f'Seu novo salário, após o aumento de {aumento:.0f}% é de R${novoSalario:.2f}')

print('Obrigada pela preferência! Até a próxima :)')