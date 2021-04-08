x = int(input("Digite um número: "))
answ = True
for i in range(1, x):
    if(i > 1) and (i != x):
        if(x % i == 0):
            answ = False
print(answ)