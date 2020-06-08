#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#  Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

Valor = int(input('Digite um número entre 0 e 99: '))
PorExtenso = ''

while True:
    if Valor >= 0 and Valor <= 99:
        break
    else:
        Valor = int(input('Tente novamente.Digite um número entre 0 e 99: '))

ExtensoUnidade = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove')
ExtensoDezena = ('Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezes', 'Dezes', 'Dez', 'Deze', 'Vinte', 'Vinte e ',
                 'Trinta e ', 'Quarenta e ', 'Cinquenta e ', 'Sessenta e ', 'Setenta e ', 'Oitenta e ', 'Noventa e ')
ExtensoDezenaDez = ('Trinta', 'Quarenta', 'Cinquenta', 'Sessenta', 'Setenta', 'Oitenta', 'Noventa')

ContadorU = Valor - ((Valor // 10)*10)

if Valor >= 11 and Valor <= 15 or Valor == 10:
    PorExtenso = ExtensoDezena[ContadorU]
elif Valor < 10:
    PorExtenso = ExtensoUnidade[Valor]
elif Valor > 20 and Valor % 10 == 0:
    PorExtenso = ExtensoDezenaDez[(Valor // 10) - 3]
elif Valor > 20:
    PorExtenso = ExtensoDezena[10 + (Valor // 10) - 1] + ExtensoUnidade[ContadorU]
elif Valor == 20:
    PorExtenso = 'Vinte'
else:
    PorExtenso = str(ExtensoDezena[ContadorU] + ExtensoUnidade[ContadorU]).capitalize()

print('Você digitou o número {}.'.format(PorExtenso))