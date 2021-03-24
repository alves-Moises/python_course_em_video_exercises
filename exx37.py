def binario():
    x = int(input('\033[1;36mDigite um valor: \033[m'))
    while x > 0:
        i = x % 2
        x = x // 2
        print(f'Valor: {x}')
        print(f'Resto da divisão: {i}')



def octal():
    print(1)
def hexdcml():
    print(1)

print('\033[1;36mDigite: \033[m')
print('\033[1:35m1\033[m\033[1;32m para binário\033[m')
print('\033[1:35m2\033[m\033[1:33m para hoctal\033[m')
print('\033[1:35m3\033[m\033[1:34m para hexadecimal\033[m')
resp = input('\033[1:36mO que deseja? \033[m')
if(resp == '1'):
    binario()
elif(resp == '2'):
    octal()
elif(resp=='3'):
    hexdcml()
