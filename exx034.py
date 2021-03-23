payment = float(input("Digite o \033[1;33msalario:\033[m: "))
if payment > 1250:
    aumento = 10
else:
    aumento = 15

new_payment = payment+(payment*(aumento/100))
print(f'Novo salário: \033[1;33m{new_payment}')