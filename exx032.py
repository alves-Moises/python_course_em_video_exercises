ano = int(input("Digite o ano atual: "))
if(ano%4 == 0 and ano %100 != 0 or ano %400 ==0):
    print('Ano \033[4;32mbissexto\033[m')
else:
    print('Não \033[4;31mbissexto\033[m')