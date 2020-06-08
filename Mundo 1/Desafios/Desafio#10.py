#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
real = float(input('Quantos reais vc tem na carteira?'))
print('Voce pode comprar {:.2f} dolares'.format(real/5.58))