num1 = float(input('Insira qualquer número: '))

num2 = float(input('Insira outro número: '))

num3 = float(input('Insira outro número, novamente: '))

#condicao1 = num2 == num1 + 1

#condicao2 = num3 == num2 + 1

#if condicao1 and condicao2: 
    #print('Os valores inseridos foram informados em ordem crescente')

if num1 < num2 and num2 < num3: 
    print('Os valores foram informados em ordem crescente')

else: print('Os valores não foram informados em ordem crescente')