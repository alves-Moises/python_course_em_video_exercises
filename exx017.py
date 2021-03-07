from math import sqrt
cttop = float(input('digite o valor do cateto oposto: '))
cttad = float(input('digite o valor do cateto adjacente: '))
cttop = cttop**2
cttad = cttad**2
result = sqrt(cttop+cttad)
sum = cttop+cttad
print(f'resultado: {result:.2f}')
print(f'soma: {sum}')