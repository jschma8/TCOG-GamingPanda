import random

LAYOUT = 'standard'

def crapCheck(roll):
    if roll not in [2,3,]:
        point = roll
    else:
        point = 'craps'
    return point

def boardState(roll, point):
    point = point
    winner = False
    global LAYOUT
    if LAYOUT == 'standard' and point == 'off':
        if roll in [7, 11]:
            winner = True
        else:
            point = crapCheck(roll)
    print(roll)
    print(point)
    print(LAYOUT)
    print(winner)
        

def main():
    roll = random.randint(2,12)
    boardState(roll, 'off')
if __name__ == '__main__':
    for i in range (19):
        main()
