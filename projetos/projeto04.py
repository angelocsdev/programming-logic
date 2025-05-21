'''
Escreva um programa que retorne o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

# Método 5Q's para montar um algoritmo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- salário mensal
- horas trabalhadas por mês
2. O que devo fazer com estes dados?
- usá-los para calcular o valor hora de um funcionário com o cálculo -> salário mensal / horas trabalhadas por mês
3. Quais são as restrições deste problema?
- os valores devem ser entregues somente em formato de salário por hora
4. Qual é o resultado esperado?
- o valor hora que um funcionário recebe
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
(faça essa parte em pseudocódigo)

input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal / horas_trabalhadas_por_mes
print(valor_hora)

'''

salario_mensal = int(input('Qual o seu salário mensal? '))
horas_trabalhadas_por_mes = int(input('Qual o seu total de horas trabalhadas por mês? '))
valor_hora = salario_mensal / horas_trabalhadas_por_mes
print(valor_hora)