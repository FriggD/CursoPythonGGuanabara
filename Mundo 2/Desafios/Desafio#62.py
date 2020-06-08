#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('------- GERADOR DE PA v2 -------')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a1
cont = 1
total = 0
more = 10
while more != 0:
  while cont <= total + more:
    print('{} -> '.format(a1), end='')
    a1 += r
    cont += 1
  print('\33[1m||')
  more = int(input('Quantos ter mais? '))
print('{} termos mostrados.'.format(total))