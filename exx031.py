distancia = float(input("Digite a \033[4;35mdistancia\033[m: "))
if distancia<=200:
    preco = 0.50
else:
    preco = 0.45
valor = distancia*preco
print(f'Valor a pagar: \033[2;33m{valor}\033[m')