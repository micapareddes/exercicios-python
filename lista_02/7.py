print('Apenas de brincadeira, me diga: ')

dias = int(input('Uma quantidade de dias: '))

hs = int(input('Uma quantidade de horas: '))

min = int(input('Uma quantidade de minutos: '))

seg = int(input('Uma quantidade de segundos: '))

segTotais = seg + (min * 60) + (hs * 3600) + (dias * (24 * 3600))

print(f'{dias} dia(s), {hs} hora(s), {min} minuto(s) e {seg} segundo(s) equivalem a um total de {segTotais} segundos!')