print('Será exibido todas as tabuadas do intervalo de números informados.')
primeira_tabuada_mostrada = int(input('Digite o primeiro número: '))
ultima_tabuada_mostrada = int(input('Digite o segundo número: '))

is_numero_negativo = primeira_tabuada_mostrada < 0 or ultima_tabuada_mostrada < 0
is_ultimo_maior_que_primeiro = ultima_tabuada_mostrada < primeira_tabuada_mostrada

while is_numero_negativo or is_ultimo_maior_que_primeiro:
    print('O último número informado deve ser maior ao primeiro e ambos devem ser positivos.')
    primeira_tabuada_mostrada = int(input('Digite o primeiro número: '))
    ultima_tabuada_mostrada = int(input('Digite o segundo número: '))   

numero_tabuada = primeira_tabuada_mostrada

while numero_tabuada <= ultima_tabuada_mostrada:
    
    numero_que_multiplica = 1

    print(f'Tabuada do {numero_tabuada}:')

    while numero_que_multiplica <= 10:
        resultado = numero_tabuada * numero_que_multiplica
        print(f'{numero_tabuada} x {numero_que_multiplica} = {resultado}')
        numero_que_multiplica = numero_que_multiplica + 1
    
    numero_tabuada = numero_tabuada + 1