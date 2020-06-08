#Condições Aninhadas

nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
  print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Paulo':
  print('Seu nome é bem comum no BR')
elif nome in 'Ana Cláudia Jéssica Juliana':
  print('Belo nome feminino')
else:
  print('Seu nome é normal')
print('Bom dia, {}!'.format(nome))

