#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco=int(input('Preço: '))
desc = preco - preco*0.05
print('Preço com desconto é: {}reais'.format(desc))