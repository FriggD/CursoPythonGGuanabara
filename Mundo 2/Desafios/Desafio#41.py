#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
# 1. Até 9 anos: MIRIM
# 2. Até 14 anos: INFANTIL
# 3. até 19 anos: JUNiOR
# 4. até 20 anos: SÊNIOR
# 5. Acima: MASTER

ano = int(input('Digite o ano de nascimento: '))
idade = 2020-ano

if idade <=9:
  print('MIRIM')
elif idade >9 and idade <=14:
  print('INFANTIL')
elif idade >14 and idade <=19:
  print('JUNiOR')
elif idade == 20:
  print('SÊNIOR')
else:
  print('MASTER')
