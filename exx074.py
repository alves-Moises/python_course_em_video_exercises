import random

a, b, c, d, e = random.randrange(0, 1000), random.randrange(0, 1000), random.randrange(0, 1000), random.randrange(0, 1000), random.randrange(0, 1000),
tup = (int(a), int(b), int(c), int(d), int(e))
print(tup)
menor = 1001
maior = 0
i = 0
for i in tup:
    print(i)   
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    i += 1

print(f'Maior: {maior}')
print(f'Menor: {menor}')