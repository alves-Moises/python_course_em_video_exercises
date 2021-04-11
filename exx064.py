x = int()
res = 0
i = 0
while x != 100:
    print('=' * 20)
    x = int(input('Digite um valor:'))
    res += x
    print(res)
    i += 1

print('+' * 20)
print(f'Total de parcelas: {i}')
print(f'Total: {res}')