import random

doors = {'a': 0, 'b':0, 'c' : 0}


win = 0
loose = 0

for i in range(10000000):
    ran_key = random.choice(list(doors))
    choice1 = random.choice(list(doors))
    options = list(doors)
    if ran_key != choice1:
        options.remove(choice1)
        options.remove(ran_key)
    if ran_key == choice1:
        options.remove(choice1)

    options2 = list(doors)
    options2.remove(random.choice(options))
    options2.remove(random.choice(choice1))

    choice2 = random.choice(options2)
    # print("Gold - %s   ,   Choice 1 - %s   Choice 2 %s"  % (ran_key, choice1, choice2 ), end = "    ")
    # print(options2)
    if choice2 == ran_key:
        win += 1
    if choice2 != ran_key:
        loose += 1




    for op in doors:
        doors[op] = 0


print('Win - %s      Loose - %s' % (win, loose))
