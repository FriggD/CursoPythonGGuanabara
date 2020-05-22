#Escreva um programa que leia a velocidaade de um carro
#Se ele ultrapassar 80Km/h, mostre uma mensagem na tela digzendo que ele foi multado
#A multa vai custar R$7,00 por cada Km acima do limite

vel = float(input('Digite a velocidade: '))
if vel>80:
  print('MULTADO {}km/h'.format(vel))
  print('Valor: R${}'.format((vel-80)*7))
else:
  print('Tá de boa')