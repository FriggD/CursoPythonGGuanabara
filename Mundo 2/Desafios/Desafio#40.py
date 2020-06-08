#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: 
# 1. Média abaixo de 5,0: REPROVADO
# 2. Média entre 5,0 e 6,9: RECUPERAÇÃO
# 3. Média +7,0: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2

if m < 5:
  print('\33[31m REPROVADO')
elif m>=5 and m<6.9:
  print('\33[33m RECUPERAÇÃO')
else:
  print('\33[32m APROVADO')