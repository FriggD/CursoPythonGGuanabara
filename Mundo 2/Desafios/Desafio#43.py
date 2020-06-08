#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com com a atbela abaixo:
# 1. Abaixo de 18.5: abaixo do peso
# 2. Entre 18.5 e 25: Peso ideal
# 3. 25 até 30: Sobrepeso
# 4. 30 até 40: obesidade
# 5. Acima de 40: obesidade mórbida

alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso/(alt*alt)

if imc < 18.5:
  print('Abaixo do peso!')
elif imc >= 18.5 and imc <25:
  print('peso ideal!')
elif imc >= 25 and imc < 30:
  print('Sobrepeso!')
elif imc >=30 and imc <40:
  print('Obesidade!')
else:
  print('Obesidade mórbida!!')