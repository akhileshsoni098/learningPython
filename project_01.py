# SNAKE WATER OR GUN GAME

import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == 's' and you == 'w':
        return False
    elif comp == 'w' and you == 'g':
        return False
    elif comp == 'g' and you == 's':
        return False
    else:
        return True

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")

randNo = random.randint(1, 3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")

a = game(comp, you)

print(f"You chose {you}")
print(f"Computer chose {comp}")

if you not in ['s', 'w', 'g']:
    print("Invalid entry")
elif a == None:
    print("The game is a tie")
elif a == False:
    print("You lose the game")
elif a == True:
    print("You win the game")
