n = int(input('Digite um valor: '))
i = 0
a = 0
b = 1
while i < n:
    print(a)
    res = a + b
    a = b
    b = res
    i += 1
    #print(res)