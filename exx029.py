speed = float(input("Digite a \033[4;34mvelocidade\033[m:"))
if speed > 80:
    print('\033[1;31mMultado\033[m')
    multa = (speed-80)*7.00
    print(f'Valor da \033[4;31mmulta\033[m: R$\033[1:33m{multa}\033[m')
else:
    print('\033[4:32mVelocidade aceitável\033[m')