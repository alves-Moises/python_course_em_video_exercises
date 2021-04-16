x = 0
while x >= 0:
    x = int(input('\nDigite um valor: '))
    i = 0
    if x > 0:
        while i <= 10:
                print(f'{x} x {i}: ', x * i)
                i += 1