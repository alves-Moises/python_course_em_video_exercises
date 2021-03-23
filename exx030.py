numb = float(input("A number: "))
if (numb % 2) == 0:
    print('\033[4;32mpar\033[m')
else:
    print('\033[4;31mNão par\033[m')