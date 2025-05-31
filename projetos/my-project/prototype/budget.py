'''
**Método 5Q's para montar um algoritmo**

*Escreva um programa usando o método 50-30-20 de finanças pessoais que calcula com base no salário fornecido.*

**Analise criticamente o problema e descubra:**
*(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)*

**1. Quais são os dados de entrada necessários?**
- salário mensal
**2. O que devo fazer com estes dados?**
- pegar o salário mensal e multiplicar por 0.5 (50%), 0.3 (30%) e 0.2 (20%). E mostrar os resultados nessa sequência. O app também deve informar para que é cada porcentagem.
**3. Quais são as restrições deste problema?**
- salário precisa ser informado
**4. Qual é o resultado esperado?**
- mostrar na tela o resultado dos cálculos e dividir o salário no método 50-30-20.
**5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?**

input salario_mensal
cinquenta_porcento = salario_mensal * 0.5
trinta_porcento = salario_mensal * 0.3
vinte_porcento = salario_mensal * 0.2
resultado = cinquenta_porcento + 'é usado para necessidades básicas (aluguel, mercado, farmácia, etc),' + trinta_porcento + 'é usado para desejos e lazer, ' + vinte_porcento + 'é usado para poupança e quitação de dívidas.'
print resultado
'''

salario_mensal = float(input("Qual é o seu salário mensal? "))
cinquenta_porcento = float(salario_mensal * 0.5)
trinta_porcento = float(salario_mensal * 0.3)
vinte_porcento = float(salario_mensal * 0.2)

resultado = str(round(cinquenta_porcento, 2)) + " é usado para necessidades básicas (aluguel, mercado, farmácia, etc), " + str(round(trinta_porcento, 2)) + " é usado para desejos e lazer, " + str(round(vinte_porcento, 2)) + " é usado para poupança e quitação de dívidas."
print(resultado)