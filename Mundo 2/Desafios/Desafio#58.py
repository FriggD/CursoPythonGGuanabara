#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
comp = randint(0,10)
print('Sou seu computador, acabei de pensar em um numero entre 0 e 10')
print('Será que vc consegue adivinhar qual foi?')
acertou = False 
palpites = 0
while not acertou:
  jogador = int(input('Qual seu palpite? '))
  palpites +=1
  if jogador == comp:
    acertou = True
  else:
    if jogador < comp:
      print("Mais!")
    else:
      print('Menos')
print('Acertou mizerávi! {} palpites'.format(palpites))
