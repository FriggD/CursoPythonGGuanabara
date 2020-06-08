#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#1. O nome com todas as letras maiúsculas;
#2. O nome com todas as letras minúsculas;
#3. Quantas letras tem sem contar os espaços;
#4. Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
print('1. Nome em maiúsculo: {}'.format(nome.upper()))
print('2. Nome em minúsculo: {}'.format(nome.lower()))
nome1 = nome.split()
print('3. Quantidade de letras: {}'.format(len(nome)-nome.count(' ')))
print('4. Quantas letras tem o primeiro nome: {}'.format(len(nome1[0])))