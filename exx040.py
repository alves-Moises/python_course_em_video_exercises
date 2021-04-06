nota_1 = float(input("Dgite a primeira nota: "))
nota_2 = float(input('Digite sua segunda nota: '))
media = (nota_1 + nota_2) / 2
if media < 5:
    print('Reprovado')
elif media < 7:
    print('Recuperação')
else:
    print('Aprovado')