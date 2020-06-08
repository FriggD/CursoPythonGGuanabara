# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informse seu sexo [M/F]: ')).strip().upper()[0]
# print(sexo)

while sexo not in 'MF':
  sexo = str(input('Dados inválidos. Masculino ou Feminino')).strip().upper()[0]
print('Sexo {} registrado!'.format(sexo))