def factorial_of_number(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial

def approximate_sin(total_number_of_terms, x):
    if 0 > x or x > 1:
        return 
    
    counter = 1
    sin = x
    sign = -1

    while counter // 2 <= total_number_of_terms:
        counter += 2
        sin += sign * ( (x ** counter) / factorial_of_number(counter) )
        sign *= -1
    return sin

print(approximate_sin(3,1))

''''
O operador // em Python é a divisão inteira, enquanto o operador / é a divisão normal (também chamada de divisão flutuante). A diferença entre os dois é que a divisão inteira arredonda o resultado para o número inteiro mais próximo (em direção a zero), enquanto a divisão flutuante mantém a parte decimal do resultado.

Por exemplo, 5 // 2 resultará em 2, enquanto 5 / 2 resultará em 2.5.

Neste caso, estamos usando counter // 2 porque queremos contar o número de iterações que ocorreram. Como estamos incrementando counter em 2 a cada vez, dividir counter por 2 (usando a divisão inteira) nos dará o número de vezes que a operação foi realizada.

Se usássemos a divisão flutuante (counter / 2), ainda obteríamos um número que representa as iterações, mas ele seria um número de ponto flutuante, o que não é necessário neste caso, já que estamos apenas contando iterações e queremos um número inteiro.
'''