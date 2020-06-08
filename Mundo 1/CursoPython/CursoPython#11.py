#Cores no terminal

# ANSI -> Scape escape sequence
#       style; text; background
# \033[                         m
# style: 0(none); 1 (negrito); 4 (sublinhado); 7(inverter cores)
# text: 30(branco); 31(vermelho); 32(verde); 33(amarelo); 34(azul); 35(roxo); 36(ciano); 37(cinza)
# background: 40(branco); 41(vermelho); 42(verde); 43(amarelo); 44(azul); 45(roxo); 46(ciano); 47(cinza)

a = 3
b = 5
print('\33[32m{} e \33[31m{}'.format(a,b))
  