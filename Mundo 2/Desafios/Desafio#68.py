#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint
cont = 0
while True:
  pc = randint(0,10)
  jogador = int(input('Digite um valor: '))
  escolha = str(input('Par ou ímpar? ')).strip()[0].upper()
  if (pc + jogador)%2 == 0 and escolha == 'P':
    print('\33[1;36mJogador venceu!')
    print('pc = {}'.format(pc))
    cont += 1
  elif (pc + jogador)%2 != 0 and escolha == 'I':
    print('\33[1;36mJogador venceu!')
    print('pc = {}'.format(pc))
    cont += 1
  else:
    print('\33[1;31mPc venceu!')
    print('pc = {}'.format(pc))
    break
print(f'Vitórias consecutivas = {cont}')

# Validação de dados
# tipo = ' '
# while tipo not in 'PpIi':
#   tipo = str(input('Par ou Impar'))
