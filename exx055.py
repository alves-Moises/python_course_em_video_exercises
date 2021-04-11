peso= float(input('Digite seu peso: '))
maior = peso
menor = (peso)
for i in range(0, 3):
    peso = float(input('Digite um peso: '))
    if(maior < peso):
        maior = peso
    elif menor > peso:
        menor = peso
print(f'Maior: {maior}')
print(f'Menor: {menor}')