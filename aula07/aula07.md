### Criando soluções em Pseudocódigo do básico ao avançado

*Pergunta pessoal: Devo me tornar profissional em pseudocodigo?*

###### Tópicos:

1 - O que é Psedocódigo
2 - Alertas sobre Pseudocódigo

###### Anotações:

*Como podemos demonstrar a solução para um problema?*
- Pseudocódigo
- Fluxogramas

-> O pseudocódigo é uma descrição dos passos necessários para resolver um determinado problema em uma linguagem natural, que não está ligada diretamente a uma linguagem de programação

*Alertas sobre Pseudocódigo*

- Não é uma linguagem de programação
- A ideia toda do pseudocódigo é de escrever algo em uma linguagem natural que pode ser lida por qualquer pessoa
- Não é padronizado, pode ser escrito de várias maneiras diferentes. Não há um padrão certo ou errado de escrever.
- Não será processado por um computador
- Não substitui uma linguagem de programação real
- Deve ser usado apenas para criar uma lógica para resolver um problema e depois escrito em uma linguagem de programação real como Python, JavaScript, C#, Java...
- Não vale a pena se tornar um especialista em pseudocódigo ou em linguagens de "aprendizado" como o "portugol"

**SINTAXE DE UM PSEUDOCÓDIGO**

- input: palavra usada para receber dados do usuário
- print: exibir o resultado no console
- if condição: condicional que controla se algo deve ou não ser feito
- else: cláusula a ser executada caso nenhuma condicional if seja executada
- loop de X a Y: laço de repetição que irá iterar de X a Y
- loop de X em Y: laço de repetição que irá iterar X em uma coleção Y
- while X: laço de repetição que acontecerá enquanto uma condição for verdadeira

**Exemplo # 1 - Valor por hora**

*Crie um programa que retorne o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

Método 5Q's
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


**Exemplo #2 - Gerador de Boas-vindas**

*Crie um programa que pede ao usuário seu nome e depois o dá as boas-vindas dizendo "X seja bem-vindo", onde X é o nome do usuário.*

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

input nome_de_usuario
print nome_de_usuario + "seja bem-vindo!"


**Exemplo #3 - Exibir o maior dos dois números**

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
    print("O segundo valor é maior!)


**EXEMPLO #4 - Fatorial de um número**

*Crie um programa que recebe um número e imprime o seu fatorial.*

Método 5Q's para montar um algoritmo:
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


**EXEMPLO #5 - Some os valores de uma lista**

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


**EXEMPLO #6 - Chute o número**

*Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.*

*O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.*

Método 5Q's para montar um algoritmo:
Analise criticamente o problema e descubra:
*(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)*

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

**Resumo:** O pseudocódigo é uma descrição dos passos necessários para resolver e quebrar as partes de um problema antes de programar de fato. Você não precisa ser muito bom em matemática, só um bom pesquisador e aprendiz. Não existe pseudocódigo perfeito e é normal achar difícil no 1º momento.