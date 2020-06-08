#Crie um programa que leia o nomne de umja cidade e diga se ela começa ou não com o nome SANTO
cidade = input('Digite o nome da sua cidade: ').strip()
cid = cidade.lower().split()
print('Sua cidade é nome de santo? {}'.format('santo' == cid[0]))