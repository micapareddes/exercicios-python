print('Bem-vindo! Hoje irei lhe ajudar a qualificaro tipo de triângulo de acordo aos seus ângulos internos.')

a1 = float(input('Me diga o valor de um dos ângulos: '))

a2 = float(input('Me diga o valor de outro ângulo: '))

a3 = float(input('Me diga o valor do último ângulo: '))

soma = a1 + a2 + a3

if soma > 180: 
    print('Não é possível a existência desse triângulo, por favor, tente novamente. Obs. A soma dos ângulos não pode ser maior do que 180o')

elif soma < 90: 
    print('Os valores pertencem a um Triângulo Acutângulo, onde a soma dos ângulos é menor que 90o')

elif soma == 90:
     print('Os valores pertencem a um Triângulo Retângulo, onde a soma dos ângulos é igual a 90o')

elif soma > 90:
     print('Os valores pertencem a um Triângulo Obtusângulo, onde a soma dos ângulos é maior que 90o')
