x = int(input('Digite o \033[4;32mprimeiro\033[m valor: '))
y = int(input('Digite o \033[4;33msegundo\033[m valor: '))
z = int(input('Digite o \033[4;34mterceiro\033[m valor: '))

if (x==y or x==z or y==z):
    print('\033[1:34mValores iguais\033[m')
    if(x==y==z):
        print('\033[4;36mTodos os valores são iguais\33[m')
    elif(x==y):
        print(f'{x} e {y} são iguais')
    elif(x==z):
        print(f'{x} e {z} são iguais')
    elif(y==z):
        print(f'{y} e {z} são iguais')
else:

    if(x > y) and (x > z):
        print(f'{x}  é maior')
    elif(y > x) and (y > z):
        print(f'{y} é maior')
    elif (z > x) and (z > y):
        print(f'{z} é maior')

    if(x < y) and (x < z):
        print(f'{x} é menor')
    if(y < x) and (y < z):
        print(f'{y} é menor')
    if(z< x) and (z < y):
        print(f'{z} é menor')





