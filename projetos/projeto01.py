# EXEMPLO 5 - Fatorial de um número
'''
Crie um programa que recebe um número e imprime o seu fatorial.

# Método 5Q's para montar um algoritmo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- número
2. O que devo fazer com estes dados?
- calcular fatorial do número recebido e imprimir na tela
3. Quais são as restrições deste problema?
- deve ser um valor positivo
- deve ser um valor inteiro
4. Qual é o resultado esperado?
- imprimir o fatorial do número
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?

input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
    fatorial = fatorial * numero
print(fatorial)
'''

numero = int(input('Digite um número: '))
if numero > 0:
    fatorial = 1
    for item in range(1, numero +1):
        fatorial = fatorial * item
    print(fatorial)