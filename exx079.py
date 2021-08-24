from typing import ValuesView


def valida_int():
    valid = False
    while not valid:
        try:
            x = int(input())
        except ValueError:
            print("Valor inválido")
        else:
            valid = True
    return x

def boole(): 
    valid = False
    while not valid:
        boole = valida_int()
        if boole in [0, 1]:
            valid = True
        else:
            print('Resposta inválida')
    return boole 
            
def main():
    i = 0
    lista = []
    keep = True
    while keep:
        print(f'Digite o {i+1}ª valor:')

        x = valida_int()
        if not(x in lista):
            i += 1
            lista.append(x)

        print("\nDeseja adicionar outro vlaor? \n[ 0 ] não \n[ 1 ] sim \nR: ", end='')
        keep = boole()
    print(lista.sort())
    print(lista)

main()