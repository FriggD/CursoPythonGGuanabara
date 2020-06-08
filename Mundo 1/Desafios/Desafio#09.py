#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada
tabuada=int(input("Tabuada do numero: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )