print('Ei, se você fuma, por favor me responda o seguinte: ')

quantidadeCigarros = int( input('Quantos cigarros, em média, você fuma por dia? ') )

anosFumando = int(input('Faz quantos anos você fuma? '))

minPerdidos = ( quantidadeCigarros * 10 ) * (anosFumando * 365)

diasPerdidos = minPerdidos / (24 * 60)

print(f'Considerando a quantidade de cigarros que você fuma faz {anosFumando} anos, você perdeu um total de {diasPerdidos:.0f} dias de vida até agora.')