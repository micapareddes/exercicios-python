#código com ajuda:
def verifyIfNumInInterval(first_num, last_num, num_to_test):
    
    testing = first_num
    
    while testing <= last_num:
        
        if testing == num_to_test:
            
            return True #early return
        
        testing += 1

    return False

conta = verifyIfNumInInterval(2, 92913919231838, 7)

print(conta)

'''''
Correão ChatGPT:
----------------
"você está testando cada número no intervalo para ver se ele é igual ao número de teste, o que pode ser bastante ineficiente para intervalos muito grandes. Em vez disso, podemos simplesmente verificar se o número de teste está entre o primeiro e o último número, o que é uma operação muito mais rápida."
---------------------------------------------------------
def verify_if_num_in_interval(start, end, num_to_test):
    return start <= num_to_test <= end

--------------------------
primeiro código:
--------------------------
def interval(first_num, last_num, num_to_test):
    
    testing = first_num
    
    resultado = False
    
    while testing <= last_num:
        
        if testing == num_to_test:
            
            resultado = True
            
        testing += 1
        

    return resultado

conta = interval(2, 5, 3)

print(conta)
'''