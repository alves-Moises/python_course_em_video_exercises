resp = 'S'
i = 0
x = 0
media = 0
while resp == 'S' or resp == 's':
    x += int(input('Digite um valor: ').lower().strip())
    i += 1
    resp = input('Você quer continuar a execução? [S] [N] ')

media = x / i
print(f'Media: {media}')
