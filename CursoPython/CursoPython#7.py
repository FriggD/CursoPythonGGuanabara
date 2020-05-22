#Operações aritméticas
# + adição
#  - subtração
#  * multiplicação
#  / divisão
# ** pow() Potencia
# // divisão inteira
# % Resto da divisão

#Ordem de precedência
#1. ();
#2. **;
#3. *; /; //; %;
#4. +; -;

nome = input('Qualé seu nome?')
print('='*20)
print('Prazer em te conhecer {}!!!'.format(nome))
print('Assim fica seu nome com 20 caracteres {:20}!!!'.format(nome))
print('Assim fica com alinhamento à direira {:>20}!!!'.format(nome))
print('Assim fica com alinhamento à esquerda {:<20}!!!'.format(nome))
print('Assim fica centralizado {:^20}!!!'.format(nome))
print('Assim fica centralizado e com caracteres{:-^20}!!!'.format(nome))
print('='*40)
#####################################
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
pot = n1 ** n2
potf = pow(n1, n2)
div = n1 // n2
res = n1 % n2
#{.3f} = 3casa flutuantes
#Caso usou dois print() e queira unir eles: ,end=' '
print('Soma: {}; subtração: {};\n multiplicação: {};\n divisão: {:.3f};\n potencia: {};\n função pow: {};\n divisão inteira: {};\n resto da divisão: {}; '.format(s, sub, m, d, pot, potf, div, res))
print('='*20)