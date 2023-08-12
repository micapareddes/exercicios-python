entrada_caracter = int(input('Qual seu número favorito: '))

if entrada_caracter <= 0:
    print('O número não pode ser zero nem negativo.')

else:
    contador = 0
    contador_a = 0
    contador_b = 0
    contador_c = 0
    seq_caracteres = ''
    
    while entrada_caracter > len(seq_caracteres):

        while contador < 3 and entrada_caracter > len(seq_caracteres):
                contador += 1
                seq_caracteres += 'A'
                contador_a +=1

        contador = 0

        while contador < 3 and entrada_caracter > len(seq_caracteres):
                contador += 1
                seq_caracteres += 'B'
                contador_b += 1 

        contador = 0

        while contador < 3 and entrada_caracter > len(seq_caracteres):
                contador += 1
                seq_caracteres += 'C'
                contador_c += 1

        contador = 0

    total = len(seq_caracteres)

    print(f'{seq_caracteres}')
    
    print(f'Foram exibidas {contador_a} letras A, {contador_b} letras B e {contador_c} letras C. Total de caracteres exibidos: {total}.')