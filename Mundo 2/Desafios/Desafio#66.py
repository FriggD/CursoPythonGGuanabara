# Cie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999. No final, mostre quantos números foram digitados e qual foi a soma entre eles

n = cont = soma = 0
while True:
  n = int(input('Digite um número: '))
  if n == 999:
    break
  soma += n 
  cont += 1
print(f'''
Soma = {soma}
Qtdade de Números = {cont}
''')
