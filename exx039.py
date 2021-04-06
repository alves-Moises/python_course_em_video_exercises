idade = int(input('Digite sua idade: '))
if idade < 18:
    tempo = 18 - idade
    if idade < 17:
        print(f'Faltam {tempo} anos para você se apresentar.')
    else:
        print(f'Falta {tempo} ano para você se apresentar.')
elif idade == 18:
    print('Está na hora de se apresentar.')
elif idade > 18:
    tempo = idade - 18
    if tempo == 1:
        print(f'Está {tempo} ano atrasado')
    else:
        print(f'Está {tempo} anos atrasado')