#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem formar um triangulo

print('-='*20)
print('Analisador de TRIANGULOS Δ')
a = float(input('Primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('terceiro segmento: '))

if a<b+c and b<a+c and c<a+b:
  print('Formou um triangulo Δ')
else:
  print('Não forma triangulo ')

