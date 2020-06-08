#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.

brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('\n{:=^30}'.format(' BRASILEIRÃO 2018 '))
print(f'Lista de timesdo Brasileirão 2018 {brasileirao}')  
print('-'*15)
print(f'Os 5 primeiros são: {brasileirao[:5]}')
print('-'*15)
print(f'Os 4 ultimos times são: {brasileirao[-4:]}')
print('-'*15)
print(f'Times em ordem alfabetica {sorted(brasileirao)}')
print('-'*15)
print(f'A chapecoense está na posição {brasileirao.index("Chapecoense")}')