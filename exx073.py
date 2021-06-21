positions = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto ', 'setimo', 'oitavo', 'nono', 'rdecimo', 'decimo_primeiro', 'decimo_seg', 
        'decimo_teceiro', 'decimo_quarto', 'decimo_quinto', 'decimo_sexto', 'decimo_sexto', 'decimo_setimo', 'decimo_nono', 'vigesimo']
i = 0
while i < 5:
    print('a)', positions[i])
    i += 1
i = 0
while i > -4:
    i -= 1
    print(positions[i])

print(f'ordem alfabética : {sorted(positions)}')

print(positions.index('segundo'))