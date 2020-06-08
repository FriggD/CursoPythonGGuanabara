#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 's' 
soma = quant = media = maior = menor = 0
while resp in 'Ss':
  num = int(input('Digite um numero: '))
  soma += num
  quant += 1
  if quant == 1:
    maior = menor = num
  else:
    if num > maior:
      maior = num
    elif num < menor:
      menor = num
  resp = str(input('Quer continuar?[S/N]? ')).strip()[0].upper()
media = soma/quant
print('''Soma = {}
        Média = {}
        Maior = {}
        Menor = {}
'''.format(soma,media, maior, menor)) 