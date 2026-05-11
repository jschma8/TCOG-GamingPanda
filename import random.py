import random

pool_start = 1000
bet_on_l12 = 30
unit = 5
min_bet = 15
win_counter = 0
loss_counter = 0
overall = 0
for j in range(1000000):
    
    win_counter = 0
    loss_counter = 0
    for i in range(100000):
        pool_start = 500
        while_break = 0
        pool = pool_start

        while while_break == 0:

            number = random.randint(1,38)
            pool = pool - bet_on_l12
            if number <= 18:
                pool = pool + (2 * bet_on_l12)

                bet_on_l12 = bet_on_l12 - unit
            else:
                bet_on_l12 = bet_on_l12 + unit   




            if pool <= 0:
                while_break = 1
                loss_counter += 1
            if pool >= 900:
                while_break = 1
                win_counter += 1 

            if bet_on_l12 < min_bet:
                while_break = 1
                win_counter += 1 

    if win_counter >= loss_counter:
        overall += 1
    else:
        overall += -1
overall =  round(overall/(10000000*10000)*100,3)
print(f"overall {overall}%")
