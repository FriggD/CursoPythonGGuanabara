# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

contIdade = sexoM = pedo = 0
while True:
  print('\33[4;35mCadastrar pessoa')
  print('_'*30)  
  idade = int(input('\33[0mIDADE: '))
  sexo = str(input('SEXO [M/F]: ')).strip()[0].upper()
  continuar = str(input('Quer continuar? [S/N]')).strip()[0].upper()
  if idade > 18:
    contIdade += 1
  if sexo == 'M':
    sexoM += 1
  if sexo == 'F' and idade < 20:
    pedo += 1
  if continuar == 'N':
    break
print(f''' 
Maior de 18: {contIdade}
Homens: {sexoM}
Mulheres menores de 20 anos: {pedo}
''')      