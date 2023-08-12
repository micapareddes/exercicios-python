prova_um = float(input('Informe sua nota da primeira prova: '))
prova_dois = float(input('Informe sua nota da segunda prova: '))
trabalho_pratico = float(input('Informe sua nota do trabalho prático: '))
media_excercicios = float(input('Informe a média das suas notas dos exercícios: '))
total_aulas = int(input('Informe o número total de aulas tidas: '))
presenca = int(input('Informe sua presença nas aulas: '))

notas = prova_um and prova_dois and trabalho_pratico and media_excercicios
notas_invalidas = notas < 0 or notas > 10

aulas_invalidas = total_aulas < 14 or total_aulas > 16

presenca_invalida = presenca < 0 or presenca > total_aulas

if notas_invalidas or aulas_invalidas or presenca_invalida:
    print('entrada inválida')

else:
    presenca_suficiente = presenca >= ( ( total_aulas * 75 ) / 100 )

    if presenca_suficiente:
        media_provas = ( prova_um + prova_dois ) / 2
        media_final = ( media_provas * 0.7 ) + ( media_excercicios * 0.1 ) + ( trabalho_pratico * 0.2 )
        if media_final >= 5.5:
            print(f'FS, Aprovado, MF: {media_final}')
        else:
            print(f'FS, Reprovado, MF: {media_final}')

    else:
        print('FI')