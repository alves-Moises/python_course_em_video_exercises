# name = input('Type your name: ')
# print(f'Uppercase: {name.upper()}')
# print(f'Down: {name.lower()}')
# print(name[:3])

def tirar_espaco(a):
   #codigo aqui
    #nova = '0'
    print(a.upper())
    print(a.lower())
    space = a.count(' ')
    leng = len(a) - space
    print(f'Tamanho total sem espaco:: {leng}')
    print(f'tamanho totla com espaço: {len(a)}')
    i = 0
    nova = [ ]
    while a[i] != ' ':
        nova.extend(a[i])
        i += 1


    print(f'nova1: {nova}')
    print(f'Novo tamanho: {len(nova)}')
    while i < leng:
        i += 1


#inicio do codigo

nomec = str(input("Digite seu Nome inteiro:  \n"))
tirar_espaco(nomec)

