#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número splicitado for negativo
n = 0
pritn('### TABUADA V3 ###')
while True:
  n = int(input('Digite um valor: '))
  if n < 0:
    break 
  print('_'*30)
  for tab in range(0,11):
    print(f'{n} x {tab} = {n * tab}')
  print('_'*30)
print('Programa encerrado!')
