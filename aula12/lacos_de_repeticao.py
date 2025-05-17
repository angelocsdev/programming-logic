# Laços de Repetição + Listas

for palavra in range(1,4):
    print('Carregando')

'''
for item in coleção
    expressão
'''
for item in range(1,20): # você pode especificar em range que número você vai iniciar, porém ele não inclui o último número
    print(item)

for item in range(1,21, 2): # (primeiro número, segundo número, valor de pulo entre os números)
    print(item)

nomes = ['João, Cristina, Gabriel, Eduarda, Jennifer, Pedro, Yan'] # coleção
for nome in nomes: # laço de repetição nome em nomes
    print(nome)