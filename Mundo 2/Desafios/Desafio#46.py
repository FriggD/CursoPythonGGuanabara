#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com pausa de um segundo entre eles
from time import sleep

for i in range(10,0,-1):
  print(i)
  sleep(1)
print('\33[31m\|/BOOM\|/'*5)

