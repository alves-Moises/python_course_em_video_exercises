lista = []
i = 0
par = []
while i < 4:
    lista.append(input('Digite um valor:'))
    i += 1

noves = 0
tup = (int(lista[0]), int(lista[1]), int(lista[2]), int(lista[3]))
print(tup)
i = 0

for i in tup:
    if i == 9:
        noves += 1
    if i % 2 == 0:
        par.append(i)

i = 0
tres = 0
valid = False
while i < 4 and (valid != True):
    if tup[i] == 3:
        tres = i
        valid = True
    i += 1
    

print('nove onde?: ', noves)
print('par?', par)
print('onde foi tres? ', tres)

