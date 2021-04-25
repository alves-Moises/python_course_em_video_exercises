def main():
    x = inpt()
    x_dec = x
    um = 0
    dois = 0
    cinco = 0
    dez = 0
    vinte = 0
    cinquenta = 0

    while x_dec >= 50:
        x_dec -= 50
        cinquenta += 1
        print(x_dec)
        
    while x_dec >= 20:
        x_dec -= 20
        vinte += 1
        print(x_dec)

    while x_dec >= 10:
        x_dec -=10
        dez += 1
        print(x_dec)

    while x_dec >= 5:    
        x_dec -= 5
        cinco += 1
        print(x_dec)

    while x_dec >= 2:
        x_dec -= 2
        dois += 1
        print(x_dec)

    while x_dec >= 1:
        x_dec -= 1
        um += 1

    print('x' * 50, f'\nx: {x}')
    print(f'\nnotas de cinquenta: {cinquenta}')
    print(f'\nnotas de vinte: {vinte}')
    print(f'\nnotas de dez: {dez}')
    print(f'\nnotas de cinco: {cinco}')
    print(f'\nnotas de dois: {dois}')
    print(f'\nnotas de um: {um}')

def inpt():
    print('x' * 50)
    valid = False
    while not valid:
        try:
            x = int(input('Digite um valor a sacar:'))
        except ValueError:
            print('Valor inválido. Digite novamente')
        else: 
            valid = True
    print('x' * 50)
    return x

main()
