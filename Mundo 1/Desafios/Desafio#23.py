#Faça um programa que leia um número de 0 à 9999 e mostre na tela cada um dos numeros separados


## Funciona apenas com os 4 numeros
# num = int(input('Digite um número de 0 à 9999'))
# n=str(num)
# print('Analisando o numero: {}'.format(num))
# print('Unidade: {}'.format(n[3]))
# print('Dezena: {}'.format(n[2]))
# print('Centena: {}'.format(n[1]))
# print('Milhar: {}'.format(n[0]))

#Maneira matemática
num = int(input('Digite um número de 0 à 9999'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero: {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))