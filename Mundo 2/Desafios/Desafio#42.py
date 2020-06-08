#Refaça o DESAFIO 35  dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# 1. Equilátero: todos os lados iguais
# 2. Isósceles: dois lados iguais
# 3. Escaleno: todos os lados diferentes

print('-='*20)
print('Analisador de TRIANGULOS Δ')
a = float(input('Primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('terceiro segmento: '))

if a<b+c and b<a+c and c<a+b:
  print('Formou um triangulo Δ')
  if a==b and a==c:
    print('Triangulo equilátero')
  elif (a == b and a != c) or (a == c and a != b):
    print('Triangulo isósceles')
  else:
    print('Triangulo escaleno')  
else:
  print('Não forma triangulo ')
