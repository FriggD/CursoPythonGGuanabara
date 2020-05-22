#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2
larg=float(input('Qual a largura em metros?'))
alt=float(input('Qual a altura em metros?'))
print('A área é de {}m2,'.format(larg*alt))
print('Será necessário {}l de tinta'.format((larg*alt)/2))