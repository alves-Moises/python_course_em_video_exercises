import  random

def ppt():
    resp_2 = ['pedra', 'papel', 'tesoura']
    resp_2 = random.choice(resp_2)
    resp = input('pedra, papel ou tesoura?').lower().strip()
    #print(resp)
    if (resp == resp_2):
        print('empate')
        ppt()
    else:
        if(resp == 'pedra' and resp_2 == 'tesoura') or (resp == 'tesoura' and resp_2 == 'papel') or (resp == 'papel' and resp_2 =='pedra'): #vitoria
            print('Vitória')
            ppt()
        else:
            print('Derrota')
            ppt()
ppt()
