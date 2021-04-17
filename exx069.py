
def main():
        better = 0     # > 18
        sum_age = 0    # total age 
        age = 0        # actual age
        answ = 'y'
        male = 0   
        male_count = 0
        woman_b = 0
        while answ == 'y':

            age = quest_age()
            sum_age += age
            better += fun_age(age, better)
            print('better age: ', better, '\n', 'x' * 30) #imprimir se eh maior de idade
            sex = answ_sex().lower()
            male = male_c(sex)
            male_count += int(male)
            if not male:
                woman_b += woman_fun(age)
            


            print('mans?', male_count)
            print('young girls?', woman_b)


            answ = answ_quest().lower()
        print('x' * 30)
        print(f'Better 18? {better}')
        print('-' * 30)
        print(f'males? {male_count}')
        print('-' * 30)
        print(f'young girs? {woman_b}')

def quest_age(): # age?
    print('=' * 30)
    valid = False
    while not valid or x < 0:
        try:
            x = int(input('Years old: '))
        except ValueError:
            print('Invalid Value')
        else:
            valid = True    
    print('=' * 30)
    return(x)

def answ_quest(): #continue?
    answ = str(input('\ndo you wanna continue? [y] [n] '))
    return(answ)

def fun_age(x, y): #better 18
    i = 0
    if x >= 18:
        i += 1
    print(i)
    return(i)

def answ_sex(): #sex?
    valid = False
    sex = ''
    while not valid:
        try:
            sex = input('sex? [m] [f] ').lower()
        except ValueError:
            print('error')
        else:
            if(sex == 'm' or sex == 'f'):
                valid = True
            else:
                print('Invalid')
    return(sex)

def male_c(i):
    valid = False
    if(i == 'm'):
        valid =  True
    return(valid)

def woman_fun(x):
    valid = False
    if x <20:
        valid = True
    return(valid)

main()
