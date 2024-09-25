from random import randint

class Character:
    def __init__(self,strength, intelligence, constitution, dexterity, name):
        self.strength = strength
        self.intelligence = intelligence
        self.constitution = constitution
        self.dexterity = dexterity
        self.name = name

def RandomiseBadGuy():
    additionalBGPoints = 21
    while additionalBGPoints > 0:
        randomAttribute = randint(1,4)
        if randomAttribute == 1:
            enemy.strength += 1
        elif randomAttribute == 2:
            enemy.intelligence += 1
        elif randomAttribute == 3:
            enemy.constitution += 1
        else:
            enemy.dexterity += 1
        additionalBGPoints -= 1
    print(f'{enemy.strength}|{enemy.intelligence}|{enemy.constitution}|{enemy.dexterity}')

player = Character(8,8,8,8, "Joe")
enemy = Character(8,8,8,8, "BadGuy")
RandomiseBadGuy()

"""
additionalPoints = 21
while additionalPoints > 0:
    value = input("What stat would you like to increase? [S|I|C|D]").upper()
    if value[0] == "S":
        print("point added to strength")
        player.strength += 1
        additionalPoints -= 1
    elif value[0] == "I":
        print("point added to intelligence")
        player.intelligence += 1
        additionalPoints -= 1
    elif value[0] == "C":
        print("point added to constitution")
        player.constitution += 1
        additionalPoints -= 1
    elif value[0] == "D":
        print("point added to dexterity")
        player.dexterity += 1
        additionalPoints -= 1
    else:
        print("invalid choice")
"""

#### BATTLE!!
while player.constitution > 0 and enemy.constitution > 0:
    randomChance = randint(1,(100 + player.intelligence - enemy.intelligence))
    if randomChance > 50:
        #player hit
        attackPower = randint(0,enemy.strength)
        blockDamage = randint(0,player.dexterity)
        player.constitution -= (attackPower - blockDamage)
        print(f' Player hit for {attackPower}, {blockDamage} blocked. {player.constitution} health remaining.')
    else:
        #enemy hit
        print(f'finish the enemy hit event')
    
    response = input("Fight or Run away? [F|R] ").upper()
    if response[0] == "R":
        break
    else:
        randomChance = randint(1,10)
        if randomChance == 1:
            print("You find a half eaten donut on the ground")
            print("+5 constitution")
            player.constitution += 5