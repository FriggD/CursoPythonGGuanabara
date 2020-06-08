#Listas (pt1)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2,0)
num.pop()
num.pop(2)
num.remove(2) #remove apenas o primeiro elemento

if 4 in num:
  num.remove(4)
else:
  print('Não tem')

print(num)
print(len(num))

val = list()
# val = []
val.append(5)
val.append(4)
val.append(6)
val.append(1)
val.append(0)

for c, v in enumerate(val):
  print(f'{c}. {v}!')

for cont in range(0,5):
  val.append(int(input('Digite um valor: ')))



a = [2, 3, 4, 6]
b = a  #cria-se uma ligação
b[2] = 8

#cópia
a = [2, 3, 4, 6]
b = a[:]