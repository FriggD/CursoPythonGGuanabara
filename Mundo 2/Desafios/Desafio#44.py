#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento
# 1.à vista dinheiro/cheque: 10% de desconto
# 2.à vista no cartão: 5% de desconto
# 3. até duas vezes no cartão: preço normal
# 4. 3x ou mais no cartão: 20%de juros

valor = float(input('Qual o valor do produto? '))
pag = int(input('Como pretende pagar:\n1. À vista dinheiro ou cheque\n2. À vista no cartão\n3. Em até 2x no cartão\n4. +3x no cartão'))

if pag == 1:
  print('Método escolhido: à vista no dinheiro ou cheque')
  print('Valor a pagar: {}'.format(valor - (valor*0.1)))
if pag == 2:
  print('Método escolhido: à vista no cartão')
  print('Valor a pagar: {}'.format(valor - (valor*0.05))) 
if pag == 3:
  print('Método escolhido: em até 2x no cartão')
  print('Valor a pagar: {}'.format(valor))
if pag == 4:
  print('Método escolhido: em 3x ou mais no cartão')
  print('Valor a pagar: {}'.format(valor + (valor*0.2)))
