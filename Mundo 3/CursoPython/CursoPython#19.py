#Dicionário
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}anos') #aspas duplas dentro dos []
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

del pessoas ['sexo']
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
  print(f'{k} = {v}')

nome = "MARCADORES MOLECULARES E SUAS APLICAÇÕES NO MELHORAMENTO ANIMAL".capitalize()
print(nome)
