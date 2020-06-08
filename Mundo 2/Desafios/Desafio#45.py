#Crie um programa que faça o computador jogar JOKENPÔ com vc
# Papel, Pedra, Tesoura
from time import sleep
# Escolha do PC
import random
comp = random.randint(0,2)
itens = ('Pedra','Papel', 'Tesoura')
# print('O computador escolheu: {}'.format(itens[comp]))

# Escolha do usuário
print(''' Suas opções:
PEDRA: 0
PAPEL: 1
TESOURA: 2''')
jogador = int(input('Qual é sua jogada?'))
# 
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
#
print('.'*25) 
print('Computador jogou: {}'.format(itens[comp]))
print('Jogador jogou: {}'.format(itens[jogador]))
print('.'*25)
# 

if comp == 0:  # comp jogou pedra
  if jogador == 0:
    print('EMPATE')
  elif jogador == 1:
    print('Jogador venceu!')
  elif jogador == 2:
    print('Computador venceu!')
  else:
    print('jogada inválida')
elif comp == 1: #comp jogou papel
  if jogador == 0:
    print('Computador venceu!')
  elif jogador == 1:
     print('EMPATE')
  elif jogador == 2:
    print('Jogador venceu!')
  else:
    print('jogada inválida')
elif comp == 2: #comp jogou tesoura
  if jogador == 0:
    print('Jogador venceu!')
  elif jogador == 1:
    print('Computador venceu!')
  elif jogador == 2:
     print('EMPATE')
  else:
    print('jogada inválida')