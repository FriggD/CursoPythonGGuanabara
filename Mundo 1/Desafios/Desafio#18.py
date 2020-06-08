#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import sin, cos, tan
num = float(input('Digite um angulo: '))
seno = sin(num)
cosseno = cos(num)
tangente = tan(num)
print('seno: {}\n cosseno: {}\n tangente{}\n'.format(seno, cosseno, tangente))