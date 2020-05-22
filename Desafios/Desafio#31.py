#Desenvolva um programa que pergunte a distancia de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
# R$0,45 para viagens mais longas

distancia = float(input('Digite a distancia em km: '))
print(distancia)
if distancia <=200:
  print('Valor: R${}'.format(0.5*distancia))
else:
  print('Valor: R${}'.format(0.45*distancia))