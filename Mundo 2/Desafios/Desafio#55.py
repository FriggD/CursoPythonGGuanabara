#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
print('Digite o peso:')
for pessoas in range(1,6):
  peso = float(input('{}ª pessoa: '.format(pessoas)))
  if pessoas == 1:
    maior = peso
    menor = peso
  else:
    if peso>maior:
      maior = peso
    if peso < menor:
      menor = peso
print('Maior: {}kg'.format(maior))
print('Menor: {}kg'.format(menor))

