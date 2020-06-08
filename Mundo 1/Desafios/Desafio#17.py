#Faça um programa que leia o ccomprimento de um cateto opsto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa.   
#h²=co²+ca²
import math
cato = float(input('Digite o comprimento do cateto oposto à hipotenusa'))
cata = float(input('Digite o comprimento do cateto adjacente à hipotenusa'))
hipo = (cato**2 + cata**2)**0,5
# seno = math.sin(hipo)
# cosseno = math.cos(hipo)
# tangente = math.tan(hipo)
# print('Sabendo que o cateto oposto é {} e o cateto adjascente é {}, então a hipotenusa é {:,2f}, e seu seno {}, cosseno {} e tangente {}'.format(cato, cata, hipo, seno, cosseno, tangente))

hi = math.hypot(cato, cata)
print(hi)