#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente

nome = input('Digite seu nome completo: ').strip()
nomes = nome.split()
print('Seu primeiro nome: {}'.format(nomes[0]))
print('Seu ultimo nome: {}'.format(nomes[len(nomes)-1]))