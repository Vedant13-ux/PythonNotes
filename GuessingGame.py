from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist



def player_guess():
    guess=''
    while guess not in ['1','2','3']:
        guess=input('Pick a Number from:0,1 or 2 :')

    return int(guess)   




def check_guess(result,guess):
    if mylist[guess]=='O':
        print('You Guessed The Right Answer')
    else:
        print('You Guessed The Wrong Answer')
        print(mylist)

mylist=[' ','O',' ']
result=shuffle_list(mylist)
guess=player_guess();
check_guess(result,guess)
