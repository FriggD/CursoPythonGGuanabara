#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e 
# o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


print("=="*16)
print("           BANCO MAZZURÃO")
print("=="*16)
valor = int(input("Qual valor você quer sacar? R$ "))
total = valor
ced = 50
totced = 0
while True:
  if total >= ced:
    total -= ced 
    totced += 1
  else:
    if totced > 0:
      print(f'Total de {totced} cedulas de {ced}')
    if ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 1
    totced = 0
    if total == 0:
      break
print("=="*16)
print("Volte sempre!")



# print("=="*16)
# print("           BANCO CEV")
# print("=="*16)
# valor = int(input("Qual valor você quer sacar? R$ "))
# cedulas = valor//50
# resto = valor%50
# if cedulas > 0:
#     print("Total de {} cédulas de R$50".format(cedulas))
# cedulas = resto//20
# resto %= 20
# if cedulas > 0:
#     print("Total de {} cédulas de R$20".format(cedulas))
# cedulas = resto//10
# resto %= 10
# if cedulas > 0:
#     print("Total de {} cédulas de R$10".format(cedulas))
# cedulas = resto//1
# if cedulas > 0:
#     print("Total de {} cédulas de R$1".format(cedulas))
# print("=="*16)
# print("Volte sempre ao BANCO CEV! Tenha um bom dia!")