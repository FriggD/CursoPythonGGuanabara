# Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial
n = int(input('Digite um número: '))
# f = factorial(n)
fact = 1
num = n
while num > 0:
  print('{} '.format(num), end='')
  print(' x ' if num > 1 else ' = ', end='')
  fact *= num
  num -= 1
print('{}\n'.format(fact))
# print('{}! = {}'.format(n,f))


n = int(input('Digite um numero para calcular seu fatorial: '))
c = 0
f = 1
for c in range (1, n):
    f *= n
    n -= 1
print('Seu fatorial é {}.'.format(f))