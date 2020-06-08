#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
num=int(input('Digite um valor em metros'))
print('Em centímetros: {}cm \n em milímetros: {}mm'.format(num*100, num*1000))