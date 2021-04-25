def main():
    total_cost = 0
    better_1000 = 0
    i = 0

    play = True
    while play == True:
        name = input('name of a product: ')
        cost = input_cost(name)

        total_cost += cost

        if i == 0: 
            better_price = cost
        else:
            if cost < better_price:
                better_price = cost

        i += 1

        if cost > 1000:
            better_1000 += 1

        play = quest()
    
    print(f'Total items: {i}')
    print(f'Better price: {better_price}')
    print(f'Better 1000: {better_1000}')

def input_cost(name):
    valid = False
    while not valid:
        try:
            x = float(input(f'{name} - R$ '))
        except ValueError:
            print('Valor inválido')
        else: 
            valid = True
    return x

def quest():
    resp = input(print('Do you wanna continue? [y] [n]'    ))
    if resp.lower() == 'y':
        resp = True
    else:
        resp = False
    return resp

main()