'''
**PROJETO #6 - Some os valores de uma lista**

*Dado uma coleção de dados "idades" [15, 46, 75, 34, 23] imprima na tela a soma destes valores*

Método 5Q's para montar um algoritmo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- lista de idades
2. O que devo fazer com estes dados?
- após receber a lista de idades, devo somar cada idade com a idade anterior até chegar ao final da lista e exibir a soma de todas as idades
3. Quais são as restrições deste problema?
- apenas os valores contidos na lista devem ser adicionados
4. Qual é o resultado esperado?
- a soma de todas as idades seja exibida
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?

idades = [15, 46, 75, 34, 23]
total = 0
loop idade em idades
    total += idade
print total
'''

idades = [15, 46, 75, 34, 23]
total = 0
for idade in idades:
    total += idade
print(total)