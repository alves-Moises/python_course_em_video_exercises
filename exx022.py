# name = input('Type your name: ')
# print(f'Uppercase: {name.upper()}')
# print(f'Down: {name.lower()}')
# print(name[:3])

def tirar_espaco(a):
   #codigo aqui
    #nova = '0'
    print(a)
    leng = len(a)
    print(f'Tamanho total:: {leng}')
    i = 0
    nova = [ ]
    while a[i] != ' ':

        nova.append(a[i])

        i += 1
    print(f'nova1: {nova}')
    print(f'Novo tamanho: {len(nova)}')
    while i < leng:
        i += 1


#inicio do codigo

nomec = input("Digite seu Nome inteiro:  \n")
tirar_espaco(nomec)

