#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

soma = menor = contK = cont = 0
prodbarato = ' '
while True:
  prod = str(input('Produto: '))
  preco = float(input('Preço: '))
  
  cont += 1 
  if preco > 1000:
    contK += 1

  if cont == 1:
    menor = preco 
    prodbarato = prod
  else:
    if preco < menor:
      menor = preco
      prodbarato = prod 

  soma += preco 
  continuar = ' '
  while continuar not in 'SsNn':
    continuar = str(input('Deseja continuar?' )).strip()[0].upper()
  if continuar == 'N':
    break   
print(f'''Total = R${soma:.2f}
Produtos que custam menos que R$1000,00: {contK}
produto mais barado: R${menor:.2f}, {prodbarato}
''')