combatMenu = {1: "Attack", 2: "Defend"}
characterLife = 100
guardianLife = 100

def combat_menu():
    global characterLife
    for key, action in combatMenu.items():
        print(key, action)
    takeAction = int(input("What do you want to do? \n "))
    if takeAction == 1:
        character_combat()
    if takeAction == 2:
        print("You embrace a defensive position. You heal up to 25 HP")
        if characterLife > 75:
            print("Your life is now 100\n ")
            characterLife = 100
        else:
            characterLife += 25
            print("Your life now is " + str(characterLife) + "\n ")
            
def guardian_combat():
    global characterLife
    import random
    attack = random.randint(1, 100)
    if attack >= 40:
        print("Guardian hits you with his sword")
        characterLife -= 10
        print("Your life now is " + str(characterLife) + "\n ")
    if attack >= 10 and attack < 40:
        print("Guardian hits you with a heavy thrust")
        characterLife -= 20
        print("Your life now is " + str(characterLife) + "\n ")
    if attack < 10:
        print("Guardian fiercely swing his sword towards your face. It's a critical hit!")
        characterLife -= 40
        print("Your life now is " + str(characterLife) + "\n ")
      
def character_combat():
    global guardianLife
    import random
    attack = random.randint(1, 100)
    if attack >= 90:
        print("You unleash a mighty blow with your axe. It's a critical hit!\n ")
        guardianLife -= 20
    if attack < 90:
        print("You hit your foe with your axe\n ")
        guardianLife -= 10

while characterLife > 0:
    combat_menu()
    if guardianLife <= 0:
        break
    guardian_combat()
    
if characterLife <= 0:
    print("You died")
if guardianLife <= 0:
    print("You have defeated the guardian")
    
