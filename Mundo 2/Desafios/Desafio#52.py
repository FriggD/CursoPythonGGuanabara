#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
num = int(input('Digite um número: '))
tot = 0
for i in range (num-1,1,-1):
  if num%i == 0:
    tot+=1
    print('\33[34m')
  else:
    print('\33[31m')
  print('{} '.format(i), end='')
print('\nO número {} foi divisível {}x'.format(num, tot))
if tot <= 1:
  print('\nÉ primo')
else:
  print('\nNão é primo!')

