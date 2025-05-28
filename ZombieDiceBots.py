print("\t \t \t Name: Jay Surya \n\t \t \t USN: 1AY24AI048 \n\t \t \t Sec: M")

import random

dice = ['brain', 'brain', 'brain', 'fire', 'fire', 'shot']

def roll(): 
    return random.choice(dice)

def zombie_dice_bot(): 
    brains = 0 
    shots = 0

    while shots < 2: 
        result = roll() 
        print("Rolled:", result)

        if result == 'brain': 
            brains += 1
        elif result == 'shot':
            shots += 1
            if shots >= 2: 
                print("Too many shots! Stop rolling.")
                break 

    print("Brains collected:", brains)

zombie_dice_bot()
