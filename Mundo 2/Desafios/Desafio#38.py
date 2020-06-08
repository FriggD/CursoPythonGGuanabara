#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# 1. O primeiro valor é maior
# 2. O segundo valor é maior
# 3. Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1>n2:
  print('Primeiro valor é maior: {}'.format(n1))
elif n2>n1:
  print('O segundo valor é maior {}'.format(n2))
else:
  print('Os dois valores são iguais')