#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quanto anos ele vai pagar.  
# Calcule o valor da prestação mensal da pretsção, sabendo que ela não pode exceder 30% do salário ou então ele será negativado

valC = float(input('Quanto sua casa custará? '))
salario = float(input('Qual seu salário? '))
prest = int(input('Em quantos anos quer pagar? '))
prestMes = valC/(prest*12)

if prestMes > (0.3*salario):
  print('Emprestimo negativado')
  print('Prestações por mes excedem 30% do seu salário: R${}'.format(prestMes))
else:
  print('Credito aprovado')
  print('As parcelas serão de R${}'.format(prestMes))