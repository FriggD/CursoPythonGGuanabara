#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
# 1. Para salários superiores a R$1250,00, calcule um aumento de 10%
# 2. Para inferiores ou iguais, o aumento é de 15%
# 

salario = float(input('Digite seu salário: '))
if salario > 1250:
  print ('seu novo salário é: {}'.format(salario + (salario*0.10)))
else:
  print ('seu novo salário é: {}'.format(salario + (salario*0.15))) 