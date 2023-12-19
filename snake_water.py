import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True


print("comp Turn : Snake(s) water(w) and gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("your Turn : Snake(s) water(w) and gun(g)?")

a = gameWin(comp, you)

print(f"comp enter {comp}")
print(f"You enter {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
