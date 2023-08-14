# Funções
def delete_student(database):
    cpf = cpf_in_database(input('Digite o cpf do aluno que deseja excluir: ').replace('.', '').replace('-', ''))

    for key in keys:
        if cpf == key:
            del database[cpf]
    print()
    print("Cadastro excluido!")
    return True

def add_students(database):
    print('Insira os dados do estudante.')
    key = valid_cpf(input('CPF: ').replace('.', '').replace('-', ''))
    name = input('Nome: ')
    age = valid_age(int(input('Idade: ')))
    bachelour = input('Curso: ')
    courses = valid_courses(input('Disciplinas: ').replace(' ', '').split(','))
    value = (name, age, bachelour, courses)
    database[key] = value
    #keys = list(student_database)

def consultate_student(database):
    print(f'Na consulta de cadastro você pode:')
    print('1. Exibir lista de estudantes cadastrados')
    print('2. Consultar estudante pelo cpf')
    print()
    consultate_action = get_valid_consultation_action(input('Digite o número da ação que deseja realizar: '))
    print()

    if valid_action(consultate_action) and consultate_action == 1:
        print('Segue abaixo a lista com todos os cadastros!')
        print()
        for key, tupla in database.items():
            print(key, tupla[:-1])
                    
        print()
        continue_enrolling = input('Digite "sim" para voltar ao menú Consulta de Cadastro: ')
    
    elif valid_action(consultate_action) and consultate_action == 2:
        cpf = cpf_in_database(input('Digite o cpf do aluno: ').replace('.', '').replace('-', ''))
        print()
        print(f'Certo! Aqui está o cadastro do cpf: {cpf} ')
        for key in database:
            if key == cpf:
                print(database[key])

def valid_action(action):
    while True:
        try:
            action = int(action)
            if action in [1, 2, 3]:
                return action
            
            elif action == 0:
                return False
            
            action = input('Por favor, escolha alguma opção do 0 até 3: ')

        except ValueError:
            action = input('Por favor, insira um número válido: ')

def valid_cpf(key):
    while len(key) != 11:
        print()
        key = input('Insira um CPF válido: ')
    while key in keys:
        print()
        print('Esse CPF já foi cadastrado!')
        key = input('Insira um cpf válido: ')
    return key

def cpf_in_database(cpf):
    while cpf not in keys:
        print()
        print('Esse CPF não foi cadastrado!')
        cpf = input('Insira um cpf válido: ')
    return cpf

def valid_age(age):
    while age <= 0:
        try:
            print()
            age = int(input('Insira idade válida: '))
        except ValueError:  # Isso será executado se a conversão para int falhar
            print()
            print("Por favor, insira um número válido para a idade.")
    return age

def valid_courses(courses):
    def repeated_courses(courses):
        size = len(courses)
        
        for i in range(size):
            for j in range(i + 1, size):
                if courses[i] == courses[j]:
                    return True
        return False
    
    while repeated_courses(courses):
        print()
        print('Entrada inválida! Não repita as disciplinas.')
        courses = input('Disciplinas: ').replace(' ', '').split(',')
    return courses

def get_valid_consultation_action(action):
    print()
    while True:
        try:
            action = int(action)

            if action in [1, 2]:
                return action  
            
            else:
                action = input('Por favor, escolha entre as opções 1 ou 2: ')

        except ValueError:
            action = input('Por favor, insira um número válido: ')


# Base de dados
student_database = {
    '12345678911': ('Micaela Pensel', 21, 'Sistemas de Informação', ['Marketing', 'Administração', 'POO']),
    '12345678900': ('Jonathan Vós', 23, 'Sistemas de Informação', ['Marketing', 'Administração', 'POO']),
    '12312312311': ('Loki Phoebe', 3, 'Doguinhos Chatos', ['Como latir alto', 'Mordidinhas', 'Beijinhos de Lingua']),
    '12345678988': ('Gordo Akali', 4, 'Gatitos Fofinhos', ['Comobagunçaracaixadeareia', 'BeijinhosAsperos', 'MiauMiau'])
    }

# Lista de chaves
keys = list(student_database)

# Pequeno sistema de cadastramento
menu = True
while menu:
    # Variável para voltar ao menú
    continue_enrolling = 'sim'

    # Menú Principal
    print()
    print('Bem vindo ao Pequeno Cadastro de Estudantes! Aqui você consegue: ')
    print()
    print('1. Adicionar estudantes')
    print('2. Remover estudantes')
    print('3. Consultar estudantes')
    print('0. Sair do programa')
    print()

    # Guarda a opção para realizar
    action = valid_action(input('Digite o número da ação que deseja realizar: '))
    print() 

    # Começa programa
    if action == 1:
            while continue_enrolling == 'sim':
                add_students(student_database)
                
                print()
                continue_enrolling = input('Digite "sim" se deseja continuar cadastrando alunos: ')
                
    elif action == 2:
        while continue_enrolling == 'sim':
            delete_student(student_database)                
            print()
            continue_enrolling = input('Digite "sim" se deseja continuar excluindo o cadastro de alunos: ')

    elif action == 3:
        while continue_enrolling == 'sim':
            consultate_student(student_database)
            print()
            continue_enrolling = input('Digite "sim" se deseja consultar outro cadastro: ')
                
    # Se action não é numero válido
    elif not valid_action(action):
        print('Programa Encerrado.')
        menu = False