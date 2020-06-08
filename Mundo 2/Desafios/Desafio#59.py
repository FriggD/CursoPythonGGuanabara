#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0 
while opcao !=5:
  print('''
  [ 1 ] SOMAR
  [ 2 ] MULTIPLICAR
  [ 3 ] MAIOR
  [ 4 ] NOVOS NUMEROS
  [ 5 ] SAIR DO PROGRAMA
  ''')
  opcao = int(input('>>>>>>> Qual sua opção? '))
  if opcao == 1:
    soma = n1 + n2
    print('{} + {} = {}'.format(n1,n2, soma))
  elif opcao == 2:
    prod = n1 * n2
    print('{} * {} = {}'.format(n1, n2, prod))
  elif opcao == 3:
    if n1 > n2:
      maior = n1 
    else:
        maior = n2 
    print('< {}'.format(maior))
  elif opcao == 4:
    print('Digite novos valores: ')
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
  elif opcao == 5:
    print('Finalizando...')
  else:
    print('Opção inválida.')
  print('=-='*10)
  sleep(2)
print('Fim!')

