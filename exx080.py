from typing import ValuesView


def valida_int():
    valid = False
    while not valid:
        try:
            x = int(input())
        except ValueError:
            print('Digite um valor válido')
        else:
            valid = True
    return x

def ordena_valor(lista, valor):
    
    lista.append(valor)   
    i = len(lista) - 1
    while i > 0:
        if len(lista) > 1:
            if lista[i] < lista[i-1]:
                temp = lista[i-1]
                lista[i-1] = lista[i]
                lista[i] = temp
        
        print(valor, 'aboc')
        i -= 1

    return lista



def main():
    lista = []
    for i in range(5):
        print(f'Digite o {i+1}ª valor:')
        x = valida_int()
        lista = ordena_valor(lista, x)
        print('a', lista)
    print(lista)
main()