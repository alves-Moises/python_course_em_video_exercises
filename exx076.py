# tupla tabulação 

listagem = ('lápis', 1.75,
            'borracha', 2,
            'caderno', 4,
            'lapisira', 2)
        
print('-' * 40)
print(f'{"listagem de preços".upper():^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print(f'R${listagem[pos]:7.2f}')

print('-' * 40)