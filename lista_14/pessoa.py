from random import *

# Functions to set random default values
def randomAge():
    return randrange(101)

def randomName():
    names_database = ['Jolanda', 'Henrique', 'Sonia', 'Laura', 'Emanuel', 'José', 'Clara', 'Tomás', 'Isabella', 'Claudio', 'Florencia', 'Fernando', 'Dalton', 'Jake', 'Phoebe', 'Chandler', 'Monica', 'Eleanor', 'Jason']
    return choice(names_database)

def randomRg():
    randomRg = ''
    for i in range(8):
        num = f'{randrange(9)}'
        randomRg += num
    return randomRg

# People
class Person():
    def __init__(self, name=randomName(), rg=randomRg(), age=randomAge()):
        self.__name = name
        self.__rg = rg
        self.__age = age

    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def updateAge(self, newAge):
        if newAge > 0:
            self.__age = newAge
            return 'Age updated successfully!'
        return 'Error'
    
    def getRg(self):
        return self.__rg

#Register
class PeopleRegistration():
    def __init__(self):
        self.__database = {}

    def addPerson(self, person):
        rg = person.getRg()
        if rg in self.__database:
            return 'Pessoa já cadastrada.'
        
        else:
            self.__database[rg] = [person.getName(), person.getAge()]
            return 'Pessoa cadastrada com sucesso.'

    def getPersonOnRegistry(self, rg):
        if rg in self.__database:
            return(f'Name: {self.__database[rg][0]}; Age: {self.__database[rg][1]}')
        
        else: return 'RG not in registry'

    def deletePersonOnRegistry(self, rg):
        if rg in self.__database:
            del self.__database[rg]
            return 'Successfully deleted!'
        
        else: return 'RG not in registry'

    def oldestPersonOnRegistry(self):
        oldest_age = -1
        for rg in self.__database:
            if self.__database[rg][1] > oldest_age:
                oldest_age = self.__database[rg][1]
                oldest_name = self.__database[rg][0]
        return f'{oldest_name}, {oldest_age}'

    def listPeopleOnRegistry(self):
        for rg in self.__database:
            print(rg, self.__database[rg][0])

# Testing code 
person1 = Person()
print(f'Nome: {person1.getName()}')
print(f'Idade: {person1.getAge()}')
print(f'Rg: {person1.getRg()}')

person2 = Person('Jony', '12345678', 23)
person3 = Person('Loki', '12345679', 26)
person4 = Person('Phoebe', '23456789', 20)

# Adding people on registry
registry = PeopleRegistration()
print(registry.addPerson(person1))
print(registry.addPerson(person2))
print(registry.addPerson(person3))
print(registry.addPerson(person4))

# Exibits person via rg
print(registry.getPersonOnRegistry('1234567'))
print(registry.getPersonOnRegistry('12345678'))

# Prints name and age of oldest on registry
print(registry.oldestPersonOnRegistry())

# Delates person via rg
print(registry.deletePersonOnRegistry('12345678'))

# Lists all people on registry
registry.listPeopleOnRegistry()