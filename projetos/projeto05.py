'''
Projeto - Gerador de Boas-vindas

Crie um programa qque pede ao usuário seu nome e depois o dá as boas-vindas dizendo "X seja bem-vindo", onde X é o nome do usuário.

Método 5Q's
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- nome do usuário
2. O que devo fazer com estes dados?
- após receber o nome do usuário, exibir a mensagem "nome do usuário + seja bem-vindo"
3. Quais são as restrições deste problema?
- devo possuir um nome para que possa exibir quem estou apresentando
4. Qual é o resultado esperado?
- uma mensagem que exibe o nome do usuário + a mensagem "seja bem-vindo"
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
(faça essa parte em pseudocódigo)
'''

nome_de_usuario = input("Qual é o seu nome? ")
print(nome_de_usuario + ", " + "seja bem-vindo!")