#Faça a tabuada
i = int(input('Digite um número: '))
f = int(input('Digite o fim da tabuada: '))
for j in range (0,f+1):
  print('{} x {} = {}'.format(i,j,(i*j)))


