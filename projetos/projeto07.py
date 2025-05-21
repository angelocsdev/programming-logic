'''
**PROJETO #7 - Exibir o maior dos dois números**

*Crie um programa que recebe dois valores e exibe qual é o maior valor entre eles.*

Método 5Q's
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- valor 1
- valor 2
2. O que devo fazer com estes dados?
- após receber os dois valores, devo compará-los e exibir qual é o maior valor entre eles.
3. Quais são as restrições deste problema?
- eu devo possuir 2 números para que a comparação seja realizada
4. Qual é o resultado esperado?
- exibir na tela o maior valor entre os dois
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
(faça essa parte em pseudocódigo)

input valor_1
input valor_2
if valor_1 > valor_2
    print("O primeiro valor é maior!")
else
    print("O segundo valor é maior!")
'''

valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))
if valor_1 > valor_2:
    print("O primeiro valor é maior!")
else:
    print("O segundo valor é maior!")