def binario():
    x = int(input('\033[1;32mDigite um valor: \033[m'))
    nova = []
    while x > 0:  #realizar divisão e pegar o resto
        i = x % 2   #resto
        x = x // 2    #valor
        # print(f'Valor: {x}')
        # print(f'Resto da divisão: {i}')


        nova.append(i)
        #print(f'Nova: {nova}')
        j = len(nova) - 1
       # print(f'J: {j}')
        while j > 0:  #
            #print('\033[1:32mx' * 20)
            #print(f'\033[mJ whie: {nova[j]}')
            aux = nova[j-1]
            nova[j-1] = nova[j]
            nova[j] = aux
            #print(f'Valor parcial: {nova}')

            j = j - 1
        #print(f'Teste: {nova}')
    print(f'\033[1:36mValor em binário: {nova}\033[m')
    pergunta()



def octal():
    x = int(input('\033[1;32mDigite um valor: \033[m'))
    nova = []
    while x > 0:  # realizar divisão e pegar o resto
        i = x % 8  # resto
        x = x // 8  # valor
        # print(f'Valor: {x}')
        # print(f'Resto da divisão: {i}')

        nova.append(i)
        # print(f'Nova: {nova}')
        j = len(nova) - 1
        # print(f'J: {j}')
        while j > 0:  #
            # print('\033[1:32mx' * 20)
            # print(f'\033[mJ whie: {nova[j]}')
            aux = nova[j - 1]
            nova[j - 1] = nova[j]
            nova[j] = aux
            #print(f'Valor parcial: {nova}')

            j = j - 1
        # print(f'Teste: {nova}')
    print(f'\033[1;35mValor em octal: {nova}\033[m')

    pergunta()
def hexdcml():
    x = int(input('Digite '))
    print(f'{hex(x)}')
def pergunta():
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
    else:
        print('Resposta inválido')
        pergunta()

pergunta()
