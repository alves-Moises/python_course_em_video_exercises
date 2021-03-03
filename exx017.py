from math import sqrt
cttop = int(input('digite o valor do cateto oposto: '))
cttad = int(input('digite o valor do cateto adjacente: '))
cttop = cttop**2
cttad = cttad**2
result = sqrt(cttop+cttad)
sum = cttop+cttad
print(f'resultado: {result}')
print(f'soma: {sum}')