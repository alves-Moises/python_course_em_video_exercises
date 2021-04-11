from random import randint
num = int(randint(0, 10))
inp = -1
# print(num)
i = 0
while inp != num:
    inp = int(input("\033[4:33m Betwwen\033[m 0 and 10: "))
    i += 1

print(f'Tentativas: {i}')