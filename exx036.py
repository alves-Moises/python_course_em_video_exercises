
valor_casa = float(input('\033[1;34mDigite o valor da casa: \033[m'))
salario = float(input('\033[1;35mDigite o seu salário: \033[m'))
tempo = float(input('\033[1:36mEm quantos anos deseja pagar? \033[m'))

meses = tempo * 12   #Calcula tempo em meses
valor_mensalidade = valor_casa / meses
if  valor_mensalidade <= (salario * (30/100)):
    print('\033[1:32mAprovado\033[m')
    print(f'\033[1:34mTempo em meses para pagar: \033[1:33m{meses}\033[m')
    print(f'\033[1:34mValor da mensalidade: \033[1:33m{valor_mensalidade}\033[m')
else:
    print('\033[1:31mReprovado\033[m')