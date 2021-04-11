def fact(i, primeiro, razao, n):
    while i < n:
        primeiro = primeiro + razao
        print(primeiro)

        i += 1

i = 0
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))  
n = 10
fact(i, primeiro, razao, n)
n = int(input('Você deseja calcular mais alguma vez? Se sim, digite  a quantidade, se não, digite 0'))

fact(0, primeiro, razao, n)
