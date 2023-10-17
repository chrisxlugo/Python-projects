import random

gamecnt = 0
wincnt = 0
losscnt = 0
tiecnt = 0

acc = input("Account name: ")
print("\nWelcome player!\n")

while True:
    n = input(f"Hi!! {acc}"
              "\nSelect option:\n"
              "(1) Player vs Player\n"
              "(2) Player vs Computer\n")
    print()
    if n == "2":
        randnum = random.randint(0, 2)
        options = ["Katana", "Knife", "Axe"]
        x = str(input("Choose your weapon (Katana, Knife, or Axe): "))
        if x in options:
            if options[randnum] == options[0] and x == options[1]:
                print(f"\n1 \n2 \n3 \nGo!!! \nYou: {options[1]}\nComputer: {options[0]} \nYou win!!\n")
                gamecnt += 1
                wincnt += 1
            elif options[randnum] == options[1] and x == options[2]:
                print(f"1 \n2 \n3 \nGo!!! \nYou: {options[2]}\nComputer: {options[1]} \nYou win!!\n")
                gamecnt += 1
                wincnt += 1
            elif options[randnum] == options[2] and x == options[0]:
                print(f"1 \n2 \n3 \nGo!!! \nYou: {options[0]}\nComputer: {options[2]} \nYou win!!\n")
                gamecnt += 1
                wincnt += 1
            elif options[randnum] == options[1] and x == options[0]:
                print(f"1 \n2 \n3 \nGo!!! \nYou: {options[0]}\nComputer: {options[1]} \nComputer wins!!\n")
                gamecnt += 1
                losscnt += 1
            elif options[randnum] == options[2] and x == options[1]:
                print(f"1 \n2 \n3 \nGo!!! \nYou: {options[1]}\nComputer: {options[2]} \nComputer wins!!\n")
                gamecnt += 1
                losscnt += 1
            elif options[randnum] == options[0] and x == options[2]:
                print(f"1 \n2 \n3 \nGo!!! \nYou: {options[2]}\nComputer: {options[0]} \nComputer wins!!\n")
                gamecnt += 1
                losscnt += 1
            else:
                print(f"1 \n2 \n3 \nGo!!! \nYou: {options[randnum]}\nComputer: {x} \nIt's a tie!\n")
                gamecnt += 1
                tiecnt += 1
        else:
            pass
            n = str(input("Would you like to keep playing? (yes/no): ")
            print("")
            if n == "yes":
                continue
            elif n == "no":
                print(f"Thank you for playing!!! \nGames played: {gamecnt} \nWins: {wincnt} \nLosses: {losscnt} \nGood Game!!")
                break
            else:
                pass
    elif n == "1":
        you = input("Choose your weapon (Katana, Knife, or Axe): ")
        computer = input("Computer's weapon (Katana, Knife, or Axe): ")

        if you not in ["Katana", "Knife", "Axe"] or computer not in ["Katana", "Knife", "Axe"]:
            print("Invalid input. Please choose Katana, Knife, or Axe.")
            continue

        if you == computer:
            print(f"1 \n2 \n3 \nGo!!! \nYou: {you}\nComputer: {computer} \nIt's a tie!\n")
            gamecnt += 1
            tiecnt += 1
        elif ((you == "Katana" and computer == "Knife") or
                (you == "Knife" and computer == "Axe") or
                (you == "Axe" and computer == "Katana")):
            print(f"\n1 \n2 \n3 \nGo!!! \nYou: {you}\nComputer: {computer} \nYou win!!\n")
        else:
            print(f"\n1 \n2 \n3 \nGo!!! \nYou: {you}\nComputer: {computer} \nComputer wins!!\n")
    else:
        pass
    n = str(input("Would you like to keep playing? (yes/no): ")
    print("")
    if n == "yes":
        continue
    elif n == "no":
        print(f"Thank you for playing!!! \nGames played: {gamecnt} \nWins: {wincnt} \nLosses: {losscnt} \nGood Game!!")
        break
    else:
        pass