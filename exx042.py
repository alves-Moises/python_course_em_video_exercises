reta_1 = int(input('Digite o valor da primeira reta: '))
reta_2 = int(input('Digite o valor da segunda reta: '))
reta_3 = int(input('Digite o valor da terceira reta: '))

# if not(((reta_1+reta_2 > reta_3) and reta_1-reta_2<reta_3) or (reta_2+reta_3 > reta_1) or (reta_2 + reta_1 > reta_2)):
if(reta_1 > (reta_2-reta_3) and reta_1 < (reta_2+reta_3) and reta_2 > (reta_1-reta_3) and reta_2 < (reta_1+reta_3) and reta_3 > (reta_1-reta_2) and reta_3 < reta_1+reta_2):
    print('\033[0;32mPode formar um triângulo')

    if(reta_1 == reta_3 == reta_2):
        print('Equilátero')
    elif(reta_1 == reta_2) or (reta_1 == reta_3) or (reta_2 ==reta_3):
        print('Isóceles')
    else:
        print('Escaleno')

else:
    print('\033[1;31mNão pode formar um triângulo')