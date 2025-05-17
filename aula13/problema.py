'''
Some os valores(exemplo com coleções)
Dados uma coleção de dados "idades" [15, 46, 75, 34, 23] imprima na tela a soma desses valores

Pseudocódigo

idades = [15, 46, 75, 34, 23]
total = 0
loop idade em idades
    total = total + idade
print total
'''

idades = [15, 46, 75, 34, 23]
total = 0
for idade in idades:
    total = total + idade
print(total)