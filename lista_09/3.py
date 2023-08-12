list = [7, 'Não te amo mais.', 'Estarei mentindo dizendo que', 'Ainda te quero como sempre quis.', 'Tenho certeza que', 'Nada foi em vão.', 'Sinto dentro de mim que', 'Você não significa nada.', 'Não poderia dizer jamais que', 'Alimento um grande amor.', 'Sinto cada vez mais que' ,'Já te esqueci!' ,'E jamais usarei a frase:' ,'EU TE AMO!', 66]

def invert_list_order(list):
    list_len = len(list)
    ind = list_len - 1

    while ind >= 0:
        print (list[ind])
        ind -= 1

print(invert_list_order(list))