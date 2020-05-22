#Escreva um programa que converta uma temperatura digitada em °C e converta para °F
celsius = float(input('Digite a temperatura em Graus Celsius: '))
fahr = (celsius * (9/5))+32
print('{} graus Fahrenheit'.format(fahr))