import random


def main(i):
    LAYOUT = 'standard'
    POINT = 'off'
    WINNER = 'no'
    BETMARKER = 'off'


    roll = random.randint(2,12)

    # bet = input('(P)ass or (NP)o Pass: ')
    # bet = str.lower(bet)

    if roll in (2,3,12):
        POINT = 'craps'
        WINNER = 'loss'

    elif roll in (7, 11):
        WINNER = 'yes'
    else:
        POINT = roll
    print(f'# is {i}')
    print(roll)
    print(LAYOUT)
    print(POINT)
    print(WINNER)
    print(BETMARKER)
    print('')

if __name__ == '__main__':
    for i in range(6):
        main(i)
