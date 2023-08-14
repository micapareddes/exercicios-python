# Entendendo como funciona
class BankAccount():
    def __init__(self, senha):
        self.__senha = senha
        self.__saldo = 0
    
    def setDeposito(self, senha, deposito):
        if senha == self.__senha and deposito > 0:
            self.__saldo += deposito
            return f'Seu deposito de R${deposito} foi realizado com sucesso!'
        else: 
            return 'Verifique que sua senha esteja correta e(ou) que o deposito seja maior que zero.' 

    def setSaque(self, senha, saque):
        if senha == self.__senha and saque <= self.__saldo and saque > 0:
            self.__saldo -= saque
            return 'Seu saque de R${saque} foi realizado com sucesso!'
        
        elif saque > self.__saldo or saque < 0:
            return 'Ops, não foi possivel realizar o saque. Verifique que o valor inserido seja menor ou igual ao saldo da sua conta.'
        
        else:
            return 'Senha incorreta.'

    def getSaldo(self, senha):
        if senha == self.__senha:
            return self.__saldo
        else:
            return 'Senha incorreta.'
        
    def changesenha(self, oldsenha, newsenha):
        if oldsenha == self.__senha:
            self.__senha == newsenha
            return 'Senha modificada com sucesso!'
        else:
            return 'Senha incorreta.'
        
    def saldoNegativo(self, senha):
        if senha == self.__senha and self.__saldo < 0:
            return True
        elif senha ==self.__senha and self.__saldo >= 0:
            return False
        else:
            return 'Senha incorreta.'
