#Condições parte 1
#Condições simples e compostas

#if carro;esquerda():
#   bloco True
# else:
#   bloco False 

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
  print('carro novo')
else:
    print('carro velho')
print('--Fim--')

#condição simplificada
#python não tem operador ternário
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo'if tempo<=3 else'carro velho')
print('--Fim--')

nome = str(input('Qual é seu nome?'))
if nome == 'Gustavo'
  print('Mazzure?')
print('Bom dia, {}!'.format(nome))


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
print('Sua média é: {}'.format(m))
if m>=7:
  print('Aprovado')
else:
  print('Reprovado')