#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('------- GERADOR DE PA v2 -------')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a1
cont = 1
while cont <= 10:
  print('{} -> '.format(a1), end='')
  a1 += r
  cont += 1
print('.')