### Aula 5 - O que são algoritmos e como montar um do zero?

*Pergunta pessoal: Como fazer algoritmos que funcionam?*

##### Tópicos:

1 - O que são algoritmos?
2 - Quando algoritmos devem ser criados?
3 - Qual é a estratégia para montar um algoritmo?
    3.1 - Método 5Q's para montar um algoritmo
    3.2 - Problema 1
    3.3 - Problema 2
    3.4 - Problema 3

##### Anotações:

**O que são algoritmos?** Uma série de instruções a serem seguidas para resolver um problema.
**Quando algoritmos devem ser criados?** Sempre que queremos montar uma sequência de passos necessários para solucionar um problema.
**Qual é a estratégia para montar um algoritmo?**

*Independente se:*

1) Quando alguém te apresenta um problema a ser resolvido.
2) Quando você encontra um problema a ser resolvido.

**Método 5Q's para montar um algoritmo**

**Analise criticamente o problema e descubra:**
*(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)*

**1. Quais são os dados de entrada necessários?**
**2. O que devo fazer com estes dados?**
**3. Quais são as restrições deste problema?**
**4. Qual é o resultado esperado?**
**5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?**

**Problema 1 - Ligar para alguém**

*Monte um algoritmo necessário para ligar para um amigo*

**1. Quais são os dados de entrada necessários?**
- um telefone
- um número de celular
**2. O que devo fazer com estes dados?**
- devo usar o celular para discar o número do meu amigo
**3. Quais são as restrições deste problema?**
- caso meu amigo não atenda, devo deixar uma mensagem dizendo "me ligue de volta
**4. Qual é o resultado esperado?**
- conseguir falar com meu amigo
**5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?**
- pegar o telefone e desbloquear
- discar o número e ligar
- esperar completar a ligação
- se o amigo atender, falar com o amigo
- se não atender, deixar a mensagem "me ligue de volta"
- finalizar a ligação


**Problema 2 - Valor por hora**

*Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.*

**1. Quais são os dados de entrada necessários?**
- salário mensal
- horas trabalhadas por mês
**2. O que devo fazer com estes dados?**
- calcular o valor hora que um funcionário recebe usando o cálculo -> salário mensal / horas trabalhadas por mês
**3. Quais são as restrições deste problema?**
- os valores devem ser entregues somente em formato de salário por hora
**4. Qual é o resultado esperado?**
- valor hora que um funcionário recebe
**5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?**
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal / horas_trabalhadas_por_mes
print(valor_hora)


**Problema 3 - Chute o número**

*Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.*
*O programa deve informar se o chute foi acima, abaixo ou igual ao valor gerado no início do programa.*

**1. Quais são os dados de entrada necessários?**
- número aleatório gerado de 1 a 10
**2. O que devo fazer com estes dados?**
- devo pegar o valor aleatório e comparar com o valor que foi chutado pelo usuário
**3. Quais são as restrições deste problema?**
- o programa não deve ser finalizado até que um valor seja chutado corretamente
- o usuário deve ser capaz de jogar quantas vezes quiser
**4. Qual é o resultado esperado?**
- o programa identificar que o valor chutado pelo usuário é igual ao valor gerado no início do programa
**5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?**
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

**Ps:** usar o método 5Q's no meu projeto pessoal antes de partir para a próxima aula.

**Resumo:** Algoritmos são uma série de instruções a serem seguidas para resolver um problema e são criados quando precisamos montar passos para solucionar um problema. Para analisar o problema pode ser usado o método 5Q's que são: 1 - dados de entrada; 2 - O que fazer com os dados; 3 - restrições do problema; 4 - resultado esperado; 5 - sequência de passos.

**Projeto Pessoal**

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
resultado = cinquenta_porcento é usado para necessidades básicas (aluguel, mercado, farmácia, etc), trinta_porcento é usado para desejos e lazer, vinte_porcento é usado para poupança e quitação de dívidas.
print resultado