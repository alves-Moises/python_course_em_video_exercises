x = int(input('Digite um valor: '))
resp = x
while x > 1:
    resp = resp * (x-1)
    x -= 1
    #print(f'X: {x}')
    print('resposta: ', resp)
