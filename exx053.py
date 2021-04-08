frase = str(input('Digite uma frase '))
assw = True
for i in range(0, len(frase)):
    # print(frase[1])
    if frase[i] != frase[(len(frase)-1)-i]:
        assw = False
print(assw)