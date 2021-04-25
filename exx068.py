import random

def main():
    win_count = 0
    win = True
    while win == True:
        print('\n', 'x' * 50,
        '''
        [1] Par
        [2] Impar\n''',
        'x' * 50)

        # inputs
        p_choice = player_input()
        p_number = player_input_numb()
        c_number = c_input_numb()

        #functions        
        print('\n', 'computer\'s number: ', c_number)
        win = int(play(p_choice, p_number, c_number, win))
        win_count += win
        print('vitoria?', win)

    print('\n', 'x' * 50, '\n', 'Numero de vitorias: ', win_count, '\n', 'x' * 50)

def player_input():
    x = 0
    valid = False
    while  not valid:
        try:
            x = int(input('\npar ou impar?[1] [2] R: '))
            if x == 1 or x == 2:
                valid = True
            else:
                print('\nValor inválido')
                valid = False
        except ValueError:
            print('Error')
    return(x)

def player_input_numb():
    valid = False
    while not valid:
        try:
            x = int(input('Digite um número: '))
        except ValueError: 
            print('Non numeric type')
        else:
            valid = True
    return(x)                               

def c_input_numb():
    x = random.randint(0, 999)
    return(x)

def play(par, x, y, win):
    result = (x + y) %  2
    print('=-' * 15, '\n', 'Resultado: ', result, '\n', '-=' * 15)
    if ((par == 1) and (result == 0)) or ((par == 2) and (result == 1)):
        print('Você venceu!\n', '=' * 30)
        valid = True
    else:
        print('Lost')
        valid = False

    return(valid)

main()
