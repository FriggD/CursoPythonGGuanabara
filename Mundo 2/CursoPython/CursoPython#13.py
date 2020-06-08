#Estrutura FOR
# Laços de repetição

# for i in range(1,10):
# não considera o ultimo numero
for i  in range (0,6):
  print('{}. Oi'.format(i))

print('*'*20)

for j  in range (6,0,-1):
  print('{}. Oi'.format(j))

print('*'*20)

for k  in range (0,7,2):
  print('{}. Oi'.format(k))

print('*'*20)

n = int(input('Digite um número: '))
for cont in range(0, n+1):
  print(cont)

print('*'*20)

i = int(input('Digite o inicio: '))
f = int(input('Digite o final: '))
p = int(input('Digite o passo: '))
for c in range(i, f+1, p):
  print(c)

print('*'*20)

s = 0
for sum in range(0,4):
  num = int(input('Digite um valor: '))
  s += num
print(s)

