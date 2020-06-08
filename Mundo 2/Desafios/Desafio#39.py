#Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
# 1. Se ele ainda vai se alistar no serviço militar
# 2. Se é hora de se alistar 
# 3. Se ja passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

ano = int(input('Digite seu ano de nascimento'))
idade = 2020 - ano

if idade <18:
  print('Ainda vai se alistar no serviço militar: falta {} '.format(18 -idade))
elif idade == 18:
  print('HORA DE SE ALISTAR!')
elif idade > 18:
  print('Passou da hora :c {}anos'.format(idade - 18))

