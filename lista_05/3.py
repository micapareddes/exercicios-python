nivel = input('Olá cliente, para ter direito ao nosso desconto, por favor, nos informe seu nível de engajamento no nosso instagram (@loja_legal123). Você é um seguidor, comentarista ou fã? ')

valor = float(input('Agora, me diga o valor da sua compra, por favor: R$'))

seguidor = valor - (valor * (5 / 100))

comentarista = valor - (valor * (8 / 100))

fa = valor - (valor * (12 / 100))

condicao1 = nivel == 'seguidor'  

condicao2 = nivel == 'comentarista'

condicao3 = nivel == 'fã'

condicao4 = valor >= 100

if condicao1 and condicao4:
    print(f'Parabéns! Você ganhou 5% de desconto na sua compra! O valor total é de R${seguidor}')

elif condicao2 and condicao4:
    print(f'Parabéns! Você ganhou 8% de desconto na sua compra! O valor total é de R${comentarista}')

elif condicao3 and condicao4:
    print(f'Parabéns! Você ganhou 12% de desconto na sua compra! O valor total é de R${fa}')

else: print(f'Sinto muito, você não é qualificado para ganhar desconto :( O valor da sua compra continua sendo R${valor}')

''''
Correção pelo ChatGPT
-----------------------

Cálculos desnecessários: Você calcula o valor de desconto para "seguidor", "comentarista" e "fã" antes mesmo de saber qual é o nível de engajamento do cliente. Estes cálculos só precisam ser feitos se o nível corresponder.

Formatando a saída: Usar a função round() para arredondar o valor da compra com desconto, para evitar muitas casas decimais no print.

Variável desnecessária: As variáveis condicao1, condicao2, condicao3 e condicao4 poderiam ser eliminadas, já que você poderia usar diretamente a condição dentro dos comandos if e elif.

------------------------

nivel = input('Olá cliente, para ter direito ao nosso desconto, por favor, nos informe seu nível de engajamento no nosso instagram (@loja_legal123). Você é um seguidor, comentarista ou fã? ')

valor = float(input('Agora, me diga o valor da sua compra, por favor: R$'))

if valor < 100:
    print(f'Sinto muito, você não é qualificado para ganhar desconto :( O valor da sua compra continua sendo R${valor}')

else:
    if nivel == 'seguidor':
        desconto = 5
        valor = valor - (valor * (desconto / 100))

    elif nivel == 'comentarista':
        desconto = 8
        valor = valor - (valor * (desconto / 100))

    elif nivel == 'fã':
        desconto = 12
        valor = valor - (valor * (desconto / 100))

    else:
        desconto = 0

    if desconto > 0:
        print(f'Parabéns! Você ganhou {desconto}% de desconto na sua compra! O valor total é de R${round(valor, 2)}')
        
    else:
        print(f'Sinto muito, você não é qualificado para ganhar desconto :( O valor da sua compra continua sendo R${valor}')

'''