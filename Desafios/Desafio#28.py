#Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
#O prgrama deverá escrever na tela se o usuário venceu ou perdeu
# 
import random
numComp = random.randint(0,5)
num = int(input('Digite um número entre 0 e 5'))
if num >=0 and num <=5: 
  if numComp == num:
    print('Acertou miseravi')
  else:
    print('Não foi dessa vez')
else:
  print('É entre 0 e 5')