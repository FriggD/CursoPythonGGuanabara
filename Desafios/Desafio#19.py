#Um professor quer sortear um dos ses quatro alunos para apagar o quadro, Faça um programa que ajude ele, lendo o nome dees e escevendo o nome do escolhido
import random
nome = random.randint(0,3)
nomes =['alno1', 'aluno2', 'aluno3', 'aluno4']
print(nomes[nome])