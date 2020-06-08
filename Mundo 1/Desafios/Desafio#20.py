#O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos>faça um programa que leia o nome dos quatro alunose mostre a ordem sorteada
import random
# nome = random.randint(0,3)
# nomes =['alno1', 'aluno2', 'aluno3', 'aluno4']
# print(nomes[nome])

n1 = str(input('Aluno 1'))
n2 = str(input('Aluno 2'))
n3 = str(input('Aluno 3'))
n4 = str(input('Aluno 4'))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('Ordem: {}'.format(lista))