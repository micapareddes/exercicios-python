'''''
Carro
-------
Métodos da classe Carro:
# Capacidade do tanque (litros)
# Quantidade de gasolina atual
# Consumo médio do combustível (km/litro)
-----------  
1. Abastece(gasolinaAbastecida):
    # recebe qnde gasolina
    # se maior do que capacidade do tanque = False
    # se gasAtual + gasAbastece é maior que capacidade = False
    # se conseguiu abastecer = True

2. informaGasolina:
    # retorna qnde gasolina atual

3. consomeGasolina(km):
    # recebe distancia
    # retorna valor gasolina após consumo médio
    # consumo não pode retornar valor negativo de combustivel

4. estaNoReserva:
    # valor de combustivel atual abaixo de 10% da capacidade do tanque = True
    # else: False
'''
# Create car via input
class Car():
    def __init__(self):
        tankCapacity = float(input('Qual a capacidade do tanque (em litros)? '))
        avarageFuelConsumption = float(input('Quantos litros de gasolina consome por kilometro? '))
        initialFuelLevel = float(input('Qual a quantidade atual de gasolina? '))
        self.__tankCapacity = tankCapacity
        self.__avarageFuelConsumption = avarageFuelConsumption
        self.__currentFuelLevel = initialFuelLevel

    def refuelCar(self):
        amountOfFuelToRefuel = float(input('Quantos litros de gasolina deseja abastecer? '))

        if amountOfFuelToRefuel > self.__tankCapacity:
            return False
        
        elif amountOfFuelToRefuel + self.__currentFuelLevel > self.__tankCapacity:
            return False
        
        else:
            self.__currentFuelLevel += amountOfFuelToRefuel
            return True
        
    def getCurrentFuelLevel(self):
        return self.__currentFuelLevel

    def setConsumedFuel(self):
        distanceCovered = float(input('Qual a distancia percorrida, em km? '))
        consumedFuel = distanceCovered / self.__avarageFuelConsumption

        if consumedFuel <= self.__currentFuelLevel:
            self.__currentFuelLevel -= consumedFuel
            return self.__currentFuelLevel
        
        else: 
            return False 

    def isFuelLevelInReserve(self):
        tenPercentOfTankCapacity = (10 * self.__tankCapacity) / 100
        
        if self.__currentFuelLevel < tenPercentOfTankCapacity:
            return True
        
        else: return False

testCar = Car()
print(testCar.refuelCar())
print()
print(testCar.getCurrentFuelLevel())
print()
print(testCar.setConsumedFuel())
print()
print(testCar.isFuelLevelInReserve())