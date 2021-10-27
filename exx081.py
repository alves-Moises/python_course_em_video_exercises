def valida_int():
    valid = False
    while not valid:
        try:
            x = int(input())
        except ValueError:
            print('Digite um valor válido: ')
        else:
            valid = True
    return x


def main():
    lista = []
    numero = True

    while numero:
        print('Digite um valor: ')
        lista.append(valida_int())
        resposta_valida = False
        while not resposta_valida:
            print('Deseja dititar mais um valor?[1] sim [2] nao')
            try: 
                resposta = int(input())
            except ValueError:
                resposta = 0

            if resposta in [1, 2]:
                resposta_valida = True
                numero = True if resposta == 1 else False
            else:
                print('Digite uma resposta valida')
    print(f'Foram digitados {len(lista)} valores')
    print(f'O valor 5 foi digitado {lista.count(5)} vezes')

main()