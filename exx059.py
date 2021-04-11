
def pergunta(x, y):
    print('''
    Digite:
    [1] Somar
    [2] Multiplicar
    [3] Maior valor
    [4] Novos números
    [5] Sair do programa
    ''')
    resp = int(input())
    if resp == 1:
        somar(x, y)
    elif resp == 2:
        multiplicar(x, y)
    elif resp == 3:
        maior(x, y)
    elif resp == 4:
        novos(x, y)
    elif resp ==5:
        print('Obrigado por utilizar o programa.')
    else: 
        print('Comando inválido. Tente novamente.')
        pergunta(x, y)

def somar(x, y):
    print('Soma: ', x + y)
    pergunta(x, y)

def multiplicar(x, y):
    print('multiplicação: ', x * y)
    pergunta(x, y)

def maior(x, y):
    if x > y:
        print(f'{x} é maior')
    elif y > x:
        print(f'{y} é maior')
    else:
        print('Valores iguais')
    pergunta(x, y)

def novos(x, y):
    x = int(input('Digite um novo valor: '))
    y = int(input('Digite outro valor: '))
    pergunta(x, y)

print('=+ ' * 5, ' +=' * 5, '\n')
x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
pergunta(x, y)
