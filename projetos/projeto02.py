'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

# Método 5Q's para montar um algoritmo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- um valor aleatório de 1 a 10
- um chute do usuário
2. O que devo fazer com estes dados?
- comparar o chute do usuário com o valor gerado e dizer se o chute foi maior, menor ou igual ao valor gerado no início
3. Quais são as restrições deste problema?
- um valor aleatório de 1 a 10
4. Qual é o resultado esperado?
- o programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?


input valor_aleatorio de 1 a 10
chute = False
input chute
if chute > valor_aleatorio:
    print('Chute foi maior que o valor gerado!')
elif chute < valor_aleatorio:
    print('Chute foi menor que o valor gerado!')
elif chute == valor_aleatorio:
    print(Você acertou!)
    chute = True
else:
    print('Chute um número de 1 a 10')
'''

import random
valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10: '))
    if chute > valor_aleatorio:
        print('Chute foi maior que o valor gerado!')
    elif chute < valor_aleatorio:
        print('Chute foi menor que o valor gerado!')
    elif chute == valor_aleatorio:
        print('Você acertou!')
        acertou = True
    else:
        print('Chute um número de 1 a 10')