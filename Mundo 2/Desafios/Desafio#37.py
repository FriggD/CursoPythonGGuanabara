#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão

num = int(input('Digite um número inteiro: '))
escolha = int(input(''' Para conversão 
Para BINÁRIO: 1 
Para OCTAL: 2 
Para HEXADECIMAL: 3 '''))
if escolha == 1:
  print('O numero {} em binário é: {}'.format(num,bin(num)[2:]))
elif escolha == 2:
  print('O numero {} em octal é: {}'.format(num, hex(num)[2:]))
elif escolha == 3:
  print('O numero {} em hexadecimal é: {}'.format(num, oct(num)[2:]))
else:
  print('escolha um numero inteiro entre 1 e 3')