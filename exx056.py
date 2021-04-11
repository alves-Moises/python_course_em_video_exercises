media = float(0)
maior = 0
menor_idade = 0
for i in range(0, 4):
    print('=-_-=' * 10)
    name = input('Digite um nome: ')
    age = int(input('Digite sua idade: '))
    sex = input('Sexo: (m/f) ').lower()
    media += age

    if sex == 'm':
        if maior < age:
            maior = age
            maior_name = name
    else:
        if age < 20:
            menor_idade += 1
media = media / 4
print('=' * 15)
print(f'Media de idade: {media}')
print(f'Homem mais velho: {maior_name}')
print(f'Quantas mulheres tem meno de 20 anos: {menor_idade}')
