#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date  
atual = date.today().year
totmaior = 0
totmenor = 0
for pes in range(1,8):
  nasc = int(input('{}ª. Digite o ano de nascimento: '.format(pes)))
  idade = atual - nasc 

  print('idade: {}'.format(idade))

  if print>=21:
    totmaior += 1
  else:
    totmenor -= 1
print('Maiores de idade: {}'.format(totmaior))
print('Menores de idade: {}'.format(totmenor))