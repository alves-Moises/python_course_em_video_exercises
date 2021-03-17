name = str(input('Your name: ')).strip()
name = name.split()
print(name[0])
print(f'Last name: {name[len(name)-1]}')
