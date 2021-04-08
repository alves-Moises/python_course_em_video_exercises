preco = float(input('Digite o valor do produto: '))
tempo = input('Digite: \n1 para pagamento a visa \n2 para pagamento a prazo \n')

if tempo == '1':
    tipo_pagamento = input('Digite:\n1 para dinheiro\n2 para chegue\n3 para cartão\n')
    if (tipo_pagamento == '1') or (tipo_pagamento == '2'):
        total = preco - (preco * 10 / 100)
    elif tipo_pagamento == 3:
        total = preco - (preco * 5 / 100)

elif tempo == '2':
    num_parcelas = int(input('Digite o número total de parcelas: '))
    if num_parcelas <= 2:
        print('Preço normal')
    else:
        total = preco + (preco * 20 / 100)

print(f"Total: {total}")
