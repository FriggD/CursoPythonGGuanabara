#cadeia de caracteres
frase = 'Curso em Vídeo Python'
print(frase[9])
print(frase[9:13])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2]) #pulando de dois em dois
print(frase[:5]) 
print(frase[15:]) 
print(frase[9::3]) #começo:final:pulos 

#análise
print(len(frase))
print(frase.count('o',0,13)) #contagem com fatiamento
print(frase.count('o'))
print(frase.find('deo')) #onde a sequencia se iniciou
print(frase.find('android')) 
print(frase.lower().find('vídeo')) 
print('Curso' in frase)

#Transformação
print(frase.replace('Python', 'Anaconda'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) #Apenas a primeira letra da frase fica em maiúscula
print(frase.title()) #Todas as iniciais de cada palavra da frase fica em maiúscula


texto = '   Aprenda Python  '
print(texto.strip()) #elimina os espaços inúteis
print(texto.rstrip()) #right => direita 
print(texto.lstrip()) #left => esquerda 

#divisão
print(texto.split())
# dividido = texto.split() 
# print(dividido[2][3]) 
print('-'.join(texto)) 

#print(""" texto beem longo """)