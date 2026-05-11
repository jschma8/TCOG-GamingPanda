import random

LAYOUT = 'standard'

def crapCheck(roll):
    if roll not in [2,3,]

def boardState(roll, point):
    point = point
    if LAYOUT == 'standard' and point != 'off':
        if roll in [7, 11]:
            winner = True
        else:
            point = crapCheck(roll)
    point = roll
    global LAYOUT
    if LAYOUT == 'standard':
        

def main():
    ...

if __name__ == '__main__':
    main()