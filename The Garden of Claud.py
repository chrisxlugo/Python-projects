import random

# Variables
ww = 5
wh = 5
enemyt = False
# Create account
acc = str(input("Account name: "))
start = str(input("Press enter to start: "))
enemy_probability = 0.8
if random.random() < enemy_probability:
    px = random.randint(0, ww - 1)
    py = random.randint(0, wh - 1)
else:
    px = random.randint(0, ww - 1)
    py = random.randint(0, wh - 1)
# Welcome
print(f"\n Welcome to Garden of Claud\n")
print(f"Hi!!! {acc}, you are in the Garden of Claud.\nYou're goal is to get out by beating Claud or running from Claud.\nGood Luck!!!!\n")
randum = random.randint(1, 5)
locations = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
enemyt = [[2, 2], [3, 3], [4, 4]]

print(f"Location: {acc} base\nWorld Boundaries:(5,5)")
nmove = int(input("How many times would you like to move? "))
for _ in range(nmove):
    move = str(input("Move (w/a/s/d): ")).lower()
    if move == 'w':
        new_x = px
        new_y = py - 1
    elif move == 'a':
        new_x = px - 1
        new_y = py
    elif move == 's':
        new_x = px
        new_y = py + 1
    elif move == 'd':
        new_x = px + 1
        new_y = py
    else:
        pass

    if 0 <= new_x < ww and 0 <= new_y < wh:
        px = new_x
        py = new_y
    else:
        pass

for x in range(2, 5):
    for y in range(2, 5):
        if px == x and py == y:
            enemyt = True
            break

# Location check after all moves are done
if enemyt:
    print(f"Careful, you are in the garden of Claud")
    dice = str(input("Would you like to roll the dice? (yes/no) "))
    randum2 = random.randint(1, 3)
    if dice == "yes":
        mob_options = ["You killed the mob", "Ran away", "You dead"]
        if mob_options[randum2] == "You killed the mob":
            print("You have beaten Claud!!!!")
        elif mob_options[randum2] == "Ran away":
            print("You are very lucky. RUN!!!")
        else:
            print("Good Game")
    elif dice == "no":
        print("What's the point of playing a game if you're scared to defeat the boss")
else:
    print(f"Congratulations {acc} you escaped the garden of Claud successfully")





