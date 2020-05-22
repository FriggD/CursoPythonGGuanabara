#Faça um programa que leia uma frase pelo teclado e mostra:
# 1. Quantas vezes aparece a letra 'A
# 2. Em que posição ela aparece a primeira vez?
# 3. Em que posição ela aparece a ultima vez

frase = input('Digite uma frase').lower().strip()
print('1. Quantidade de letras a: {}'.format(frase.count('a')))
print('2. Posição onde se iniciou os as: {}'.format(frase.find('a')))
print('3. Posição onde se finalizou os as: {}'.format(frase.rfind('a'))) #começa a procurar pela direita