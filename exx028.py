from random import randint
num = int(randint(0, 5))
# print(num)
inp = int(input("\033[4mBetwwen\033[m 0 and 5: "))
if inp == num:
    print('\033[1:32mCorrect aswer\033[m')
else:
    print('\033[1:31mWrong\033[m.')
