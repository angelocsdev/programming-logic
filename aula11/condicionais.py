# Condicionais

# if elif e else

# Situação 1

'''
E aí, bora sair hoje?
Se eu terminar o trabalho, eu consigo.
'''

trabalho_terminado = True
if trabalho_terminado == True:
    print('Bora sair!')
else:
    print('Não posso sair agora.')

# Situação 2

'''
Ei, você consegue me ajudar a mover essas caixas lá para fora hoje a tarde?
Se eu estiver livre, sim. Mas, se não der pede meu irmão para te ajudar
'''

estou_livre = False
if estou_livre == True:
    print('Ok, posso ajudar hoje sim!')
else:
    print('Peça meu irmão para te ajudar!')

# Situação 3

'''
Eu cheguei atrasado na aula, ainda posso entrar?
Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrário irá tomar uma suspensão.
'''

numero_de_atrasos = 1
if numero_de_atrasos >= 3:
    print('Você está suspenso')
elif numero_de_atrasos == 1:
    print('Pode entrar, porém caso tome mais 2 faltas, irá ser suspenso')
elif numero_de_atrasos == 2:
    print('Pode entrar mais caso tome mais 1 falta, irá ser suspenso')
else:
    print('Pode entrar')