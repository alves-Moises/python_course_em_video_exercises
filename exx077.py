# tupla com um monte de palavras
# mostrar as vogais de cada palavra

palavras = ('aprender', 'programar', 'linguagem', 'python')

for p in palavras:
    print(f'Na palavra {p} temos', end = '')

    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = '')