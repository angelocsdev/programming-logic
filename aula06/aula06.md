### Aula 6 - 4 Conceitos OBRIGATÓRIOS Para Ser Capaz De Resolver Problemas

*Pergunta pessoal: É mais importante aprender uma linguagem específica ou conseguir utilizar esses conceitos, em todas?*

###### Tópicos:

1 - 4 Conceitos OBRIGATÓRIOS
    1.1 - Variáveis
    1.2 - Condicionais
    1.3 - Laços de repetição
    1.4 - Coleções

###### Anotações:

Os conceitos OBRIGATÓRIOS são: 1 - Variáveis; 2 - Condicionais; 3 - Laços de repetição; 4 - Coleções.

1 - Variáveis -> temos uma informação que precisa ser guardada.

Problema -> Valor por hora

Variáveis do problema em negrito:

Escreva um programa que retorna o **valor hora** de um funcionário com base no seu **salário mensal** e **horas trabalhadas por mês**.

- valor hora
- salário mensal
- horas trabalhadas por mês

2 - Condicionais -> escolhas feitas com base em uma condição.

Problema -> Chute o número

Escreva um programa que, ao iniciar gera um valor aleatório de 1 à 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.
O programa deve informar se **o chute foi acima, abaixo ou igual** ao valor aleatório gerado no início do programa.

Neste caso, podemos identificar algumas condicionais:

1 - se o número chutado for menor que o número gerado, então avise que deve chutar mais alto.
2 - se o número chutado for maior que o número gerado, então avise que deve chutar mais baixo.
3 - se o número chutado for igual ao número gerado, então avise que ele acertou.

3 -> Laços de repetição: no mundo real e na programação, temos diversas situações onde precisamos fazer uma ação várias vezes ou por uma determinada quantidade de vezes. Ex: cortar um pão, varrer o chão, dar vários passos para chegar até um lugar.

-> Cenário real #1: Vamos dizer que para derrubar uma árvore, tenha que dar 11 machadadas nela. Então você teria que criar um comando que mande a pessoa dar 11 machadadas na árvore e com isso feito a árvore cairia.

-> Cenário real #2: Crie um programa que recebe um número e o incrementa por 1 por 10 vezes.
- valor = 10
- 1ª repetição | valor = valor + 1 | 11
- 2ª repetição | valor = valor + 1 | 12
- 3ª repetição | valor = valor + 1 | 13
- 4ª repetição | valor = valor + 1 | 14
- 5ª repetição | valor = valor + 1 | 15
- 6ª repetição | valor = valor + 1 | 16
- 7ª repetição | valor = valor + 1 | 17
- 8ª repetição | valor = valor + 1 | 18
- 9ª repetição | valor = valor + 1 | 19
- 10ª repetição | valor = valor + 1 | 20

Ponto em comum -> normalmente possuem um ponto inicial e um ponto final, ou em alguns casos uma condição que irá significar o final daquele laço de repetição, ex: deixe a torneira aberta até que o copo esteja cheio de água; nade até chegar ao outro lado da piscina; some todos os valores enquanto o valor for menor que 100; dê machadadas na árvore até que ela caia.
Pontos chaves -> são úteis para conseguir automatizar processos; é possível definir por quantas vezes algo deve ser executado; possuem ponto de início e fim; podem estar atrelados a uma condição.

4 - Coleções: em muitos casos, você terá a necessidade de trabalhar com coleções de valores que estão armazenados em um local só, ex:

convidados = ['Jeff', 'Amanda', 'Carol', 'Robert']
numeros_premiados = [12, 67, 34, 100, 55]

Exemplo de uso de coleções:

Dado uma coleção de dados "idades" [15, 46, 75, 34, 23] imprima na tela a soma desses valores.

- Definir o total como 0
- Passar por 1º valor e somar ele ao total
- Passar por 2º valor e somar ele ao total
- Passar por 3º valor e somar ele ao total
- Passar por 4º valor e somar ele ao total
- Passar por 5º valor e somar ele ao total
- Exibir o valor total

*"Dominar estes 4 conceitos te permitirá criar algoritmos mais facilmente."*

**Resumo:** Existem 4 conceitos OBRIGATÓRIOS para ser capaz de resolver problemas: variáveis, onde a informação é guardada; condicionais, escolhas feitas com base em uma condição; laços de repetição, usados um situações que precisamos repetir uma ação várias vezes ou por número determinado; e coleções, conjunto de valores que estão armazenados em um lugar só.