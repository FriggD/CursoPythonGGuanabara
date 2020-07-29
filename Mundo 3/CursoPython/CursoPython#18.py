#Lista pt2

teste = list()
test.append('Gustavo')
test.append(40)

galera = list()
galera.append(teste[:])

povo = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 47]]
for p in povo:
  print(p[0])

pessoas = list()     
dado = list()
for c in range(0,3):
  dado.append(str(input('Nome: ')))
  dado.append(int(input('Idade: ')))
  pessoas.append(dado[:])
  dado.clear()
print(pessoas)

totmai = totmen = 0
for p in povo:
  if p[1] >= 21:
    print(f'{p[0]} é maior de idade')
    totmai += 1
  else:
    print(f'{p[0]} é menor de idade')
    totmen += 1
print(f'maiores = {totmai}; menores {totmen}')