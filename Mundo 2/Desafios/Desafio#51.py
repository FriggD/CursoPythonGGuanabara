#Desenvolva um programa que leia o primeiro termo e a razão de um PA. No fina, mosttre os 10 primeiros termos dessa progressão
print('*-Progressão aritmética-*')
a1 = int(input('1. Digite o primeiro termo da PA: '))
r = int(input('2. Digite a razão da PA: '))
for i in range (1,11):
  print('{}ºtermo. = {}'.format(i, a1+(i-1)*r))

