#Crie um programa que leia o nomne de uma pessoa e diga se ela tem "Silva no nome"
nome = input('Digite o seu nome: ').strip()
#in é um operador do Python
print('Seu nome tem Silva? {}'.format('Silva'in nome.lower()))