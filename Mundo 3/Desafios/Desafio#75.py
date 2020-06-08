# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# Variáveis simples dentro de () formam as tuplas

num = ( 
  int(input('Digite um número: ')), 
  int(input('Digite um número: ')), 
  int(input('Digite um número: ')), 
  int(input('Digite um número: ')) 
)
print(f'Voce digitou os numeros {num}')
print(f'O valor 9 apareceu {num.count(9)}x')
if 3 in num:
  print(f'O número 3 está na posição {num.index(3)+1}.')
else:
  print('Não existe o numero 3')
for n in num:
  if n%2 == 0:
    print('Números pares: {}'.format(n))