import random
gamecnt= 0
wincnt= 0
losscnt= 0
tiecnt= 0
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
            options= ["rock","paper","scissors"]
            x = str(input("Rock, Paper, Scissors \nPick Player 1: "))
            if x in options:
                if options[randnum] == options[0] and x == options[1]:
                    print(f"\n1 \n2 \n3 \nGo!!! \nPlayer 1: {options[1]}\nComputer: {options[0]} \nPlayer 1 wins!! \n")
                    gamecnt +=1
                    wincnt += 1
                elif options[randnum] == options[1] and x == options[2]:
                    print(f"1 \n2 \n3 \nGo!!! \nPlayer 1: {options[2]}\nComputer: {options[1]} \nPlayer 1 wins!! \n")
                    gamecnt += 1
                    wincnt += 1
                elif options[randnum] == options[2] and x == options[0]:
                    print(f"1 \n2 \n3 \nGo!!! \nPlayer 1: {options[0]}\nComputer: {options[2]} \nPlayer 1 wins!! \n")
                    gamecnt += 1
                    wincnt += 1
                elif options[randnum] == options[1] and x == options[0]:
                    print(f"1 \n2 \n3 \nGo!!! \nPlayer 1: {options[0]}\nComputer: {options[1]} \nComputer wins!! \n")
                    gamecnt += 1
                    losscnt += 1
                elif options[randnum] == options[2] and x == options[1]:
                    print(f"1 \n2 \n3 \nGo!!! \nPlayer 1: {options[1]}\nComputer: {options[2]} \nComputer wins!! \n")
                    gamecnt += 1
                    losscnt += 1
                elif options[randnum] == options[0] and x == options[2]:
                    print(f"1 \n2 \n3 \nGo!!! \nPlayer 1: {options[2]}\nComputer: {options[0]} \nComputer wins!! \n")
                    gamecnt += 1
                    losscnt += 1
                else:
                    print(f"1 \n2 \n3 \nGo!!! \nPlayer 1: {options[randnum]}\nComputer: {x} \nTieeeeeeee!! \n")
                    gamecnt += 1
                    tiecnt += 1
            else:
                pass
                n= str(input("Would you like to keep playing? "))
                print("")
                if n == "yes":
                    continue
                elif n == "no":
                    print(f"Thank you for playing!!! \nGames played: {gamecnt} \nWins: {wincnt} \nLoss: {losscnt} \nGood Game!!")
                    break
                else:
                    pass
        elif n == "1":
            p1 = input("Rock, Paper, Scissors \nPick Player 1: ")
            p2 = input("Pick Player 2: ")

            if p1 not in ["rock", "paper", "scissors"] or p2 not in ["rock", "paper","scissors"]:
                print("Invalid input. Please choose Rock, Paper, or Scissors.")
                continue

            if p1 == p2:
                print(f"1 \n2 \n3 \nGo!!! \nPlayer 1: {p1}\nPlayer 2: {p2} \nTieeeeeeee!! \n")
                gamecnt += 1
                tiecnt += 1
            elif ((p1 == "rock" and p2 == "scissors") or
                    (p1 == "scissors" and p2 == "paper") or
                    (p1 == "paper" and p2 == "rock")):
                print(f"\n1 \n2 \n3 \nGo!!! \nPlayer 1: {p1}\nPlayer 2: {p2} \nPlayer 1 wins!! \n")
            else:
                print(f"\n1 \n2 \n3 \nGo!!! \nPlayer 1: {p1}\nPlayer 2: {p2} \nPlayer 2 wins!! \n")
        else:
            pass
        n = str(input("Would you like to keep playing? (yes/no): "))
        print("")
        if n == "yes":
            continue
        elif n == "no":
            print(
                f"Thank you for playing!!! \nGames played: {gamecnt} \nWins: {wincnt} \nLoss: {losscnt} \nGood Game!!")
            break
        else:
            pass


