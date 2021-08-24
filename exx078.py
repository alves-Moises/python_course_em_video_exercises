def valida_int():
    valid = False
    while not valid:
        try:
            x = int(input())
        except ValueError:
            print('Valor inválido')
        else:
            valid = True
    return x

def main():
    lista = []
    maior = 0
    for i in range(5):
        j = i + 1
        print(f'Digite o {j}ª valor')
        x = valida_int()
        lista.append(x)
        if x > maior:
            maior = x
        try:
            if menor > x:
                menor = x
        except:
            menor = x
    print(f'Maior: {maior} na posição', lista.index(maior))
    print(f'Menor: {menor} na posição {lista.index(menor)}')
    print(f'Lista: {lista[:]}')

main()