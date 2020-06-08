#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o
sum=0
for i in range(0,6):
  num=int(input('Digite um número: '))
  if num%2==0:
    sum+=num
print(sum)    

