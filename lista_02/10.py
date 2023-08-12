distancia = float( input('Me diga, qual a distância a ser percorrida? (Por favor, digite o valor em kilometros): ') )

vel = float( input('Ótimo! Agora me diga a velocidade média esperada para a viagem (Por favor, digite em km/h): ') )

tempo = distancia / vel

print(f'Você levará {tempo:.1f}hs aproximadamente, para percorrer uma distância de {distancia}km a {vel:.0f}km/h.')