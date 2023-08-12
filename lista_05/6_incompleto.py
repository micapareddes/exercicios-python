pressao = float(input('Informe o valor de pressão da agua em kPa: '))

temp = float(input('Informe o valor da temperatura da agua em °C: '))

if pressao == 100 and temp < 0:
    print('A agua se encontra em estado sólido')

elif pressao == 100 and temp == 0:
    print('A agua se encontra em estado de mistura entre sólido-líquido')

elif pressao == 100 and 0 < temp < 100:
    print('A agua se encontra em estado líquido')

elif pressao == 100 and temp == 100:
    print('A agua se encontra em estado de mistura entre líquido-vapor')

elif pressao == 100 and temp > 100:
    print('A agua se encontra em estado gasoso')

#Para p = 200 kPa
#Mistura líquido-vapor se T = 120oC
#Gasoso se T > 120oC
#Para p = 300 kPa
#Mistura líquido-vapor se T = 133,6oC
#Gasoso se T > 133,6oC
#Para p = 400 kPa
#Mistura líquido-vapor se T = 143,6oC
#Gasoso se T > 143,6oC
#Para p = 500 kPa
#Mistura líquido-vapor se T = 151,9oC
#Gasoso se T > 151,9oC

#Se o usuário entrar com valores que não constam no banco de dados, 
# exibir uma mensagem que os valores informados não constam no banco de dados.
