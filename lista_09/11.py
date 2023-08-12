def string_reader(text):
    ind = 0
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    special_char_list = [ '[', '\\', 'ˆ', ']', '_', '`' ]
    vogal_counter = 0
    cons_counter = 0
    num_counter = 0
    
    while ind < len(text):
        character = text[ind]
        if character == ' ':
            ignore = 0

        elif character > '/' and character <= '9':
            num_counter += 1

        elif character <= 'z' and character >= 'A' and character not in special_char_list:
            if character in vogais:
                vogal_counter += 1
            else: cons_counter += 1
        
        ind += 1

    return f'A string possui: {vogal_counter} vogais, {cons_counter} consoantes e {num_counter} números.'

print(string_reader('Eu amo minha namorada muito, e ela vai me esperar 5 min para dar commit e nao perder tudo oq eu fiz'))