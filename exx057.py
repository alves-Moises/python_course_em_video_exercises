sex = ''
while sex != 'm' and sex != 'f':
    sex = str(input('Digite o sexo: [m] ou [f]')).lower().strip()[0]
    print(sex)