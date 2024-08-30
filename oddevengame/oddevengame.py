def start():
    import random

    def initialize_game():
        print("This is Odd Eve game")

    def toss():
        print("Choose Odd or Even for toss")
        user_choice = input().casefold()
        
        if user_choice == "odd":
            print("You chose Odd, so I choose even.")
        elif user_choice == "even" or user_choice == "eve":
            print("You chose even, so I choose odd")
        else:
            print("You were given two options and you chose to mess it up, well congrats! \nBye!")
            quit()
        
        print("Now type any number from 1 to 10")
        Done = False
        while not Done:
            try:
                toss_inp = int(input())
                if toss_inp <= 0 or toss_inp >= 11:
                    print("Try again with a number within the given range?")
                else:
                    Done = True
            except ValueError:
                print("Try again with an actual number?")

        toss_comp_imp = random.randint(1, 10)

        if (toss_comp_imp + toss_inp) % 2 == 0:
            if user_choice == "even" or user_choice == "eve":
                print(f"Well, {toss_inp} + {toss_comp_imp} is {(toss_comp_imp + toss_inp)}, which is even. So, you win :)")
                player_toss_win()
            else:
                print(f"Well, {toss_inp} + {toss_comp_imp} is {(toss_comp_imp + toss_inp)}, which is even. So, I win :)")
                computer_toss_win()
        else:
            if user_choice == "odd":
                print(f"Well, {toss_inp} + {toss_comp_imp} is {(toss_comp_imp + toss_inp)}, which is odd. So, you win :)")
                player_toss_win()
            else:
                print(f"Well, {toss_inp} + {toss_comp_imp} is {(toss_comp_imp + toss_inp)}, which is odd. So, I win :)")
                computer_toss_win()

    def player_toss_win():
        print("What do you choose? Batting or Balling?")
        Done = False
        while not Done:
            plr_choice = input().casefold()
            if "bat" in plr_choice or "batting" in plr_choice:
                print("You chose batting... I see...")
                Done = True
            elif "ball" in plr_choice or "balling" in plr_choice:
                print("You chose Balling... I see...")
                Done = True
            else:
                print("Try again... \nBatting or Balling?")
        DaGame(plr_choice)

    def computer_toss_win():
        Options = ["batting", "balling"]
        choice = random.choice(Options)
        print(f"I choose {choice}")
        if choice == "batting":
            DaGame("balling")
        else:
            DaGame("batting")

    def DaGame(choice):
        if "bat" in choice:
            print("It's your batting. Type any number within range 1-10")
            out = False
            score = 0
            while not out:
                try:
                    inp = int(input())
                    if inp <= 0 or inp >= 11:
                        print("Try again with a number within the given range?")
                    else:
                        cmp_imp = random.randint(1, 10)
                        print(f"You chose {inp} and I chose {cmp_imp}")
                        if abs(inp - cmp_imp) == 1 or (cmp_imp == 1 and inp == 10) or (inp == 1 and cmp_imp == 10):
                            print("OUT!")
                            out = True
                        elif inp == cmp_imp:
                            print("Squared!!!")
                            score += inp * cmp_imp
                        else:
                            score += inp
                        print(f"Total score = {score}")
                except ValueError:
                    print("Try again with an actual number?")

            print(f"Your score was {score}\n\n")
            print("It's my batting now\n")

            out = False
            cmpscore = 0
            while not out:
                try:
                    inp = int(input())
                    if inp <= 0 or inp >= 11:
                        print("Try again with a number within the given range?")
                    else:
                        cmp_imp = random.randint(1, 10)
                        print(f"You chose {inp} and I chose {cmp_imp}")
                        if abs(inp - cmp_imp) == 1 or (cmp_imp == 1 and inp == 10) or (inp == 1 and cmp_imp == 10):
                            print("OUT!")
                            out = True
                        elif inp == cmp_imp:
                            print("Squared!!!")
                            cmpscore += inp * cmp_imp
                        else:
                            cmpscore += cmp_imp
                        print(f"Total score = {cmpscore}")

                        
                        if cmpscore > score:
                            print("I surpassed your score! YOU LOSE!!!\n", "L" * 100)
                            return  

                except ValueError:
                    print("Try again with an actual number?")

            print(f"My score was {cmpscore} and your score was {score}!\n")
            if score > cmpscore:
                print("YOU WIN!!!\n")
            elif score < cmpscore:
                print("YOU LOSE!!!\n", "L" * 100)
            else:
                print("Tie :/")

        elif "ball" in choice:
            print("It's my batting now\n")
            out = False
            cmpscore = 0
            while not out:
                try:
                    inp = int(input())
                    if inp <= 0 or inp >= 11:
                        print("Try again with a number within the given range?")
                    else:
                        cmp_imp = random.randint(1, 10)
                        print(f"You chose {inp} and I chose {cmp_imp}")
                        if abs(inp - cmp_imp) == 1 or (cmp_imp == 1 and inp == 10) or (inp == 1 and cmp_imp == 10):
                            print("OUT!")
                            out = True
                        elif inp == cmp_imp:
                            print("Squared!!!")
                            cmpscore += inp * cmp_imp
                        else:
                            cmpscore += cmp_imp
                        print(f"Total score = {cmpscore}")
                except ValueError:
                    print("Try again with an actual number?")

            print(f"My score was {cmpscore}\n\n")
            print("It's your batting now\n")

            out = False
            score = 0
            while not out:
                try:
                    inp = int(input())
                    if inp <= 0 or inp >= 11:
                        print("Try again with a number within the given range?")
                    else:
                        cmp_imp = random.randint(1, 10)
                        print(f"You chose {inp} and I chose {cmp_imp}")
                        if abs(inp - cmp_imp) == 1 or (cmp_imp == 1 and inp == 10) or (inp == 1 and cmp_imp == 10):
                            print("OUT!")
                            out = True
                        elif inp == cmp_imp:
                            print("Squared!!!")
                            score += inp * cmp_imp
                        else:
                            score += inp
                        print(f"Total score = {score}")
                        if score > cmpscore:
                            print("You surpassed my score! YOU WIN!!!\nGG")
                            return  

                except ValueError:
                    print("Try again with an actual number?")

            print(f"My score was {cmpscore} and your score was {score}!\n")
            if score > cmpscore:
                print("YOU WIN!!!\nGG")
            elif score < cmpscore:
                print("YOU LOSE!!!\n", "L" * 100)
            else:
                print("Tie :/")

    def play_game():
        initialize_game()
        while True:
            toss()
            while True:  
                print("Do you want to play again? (yes/no)")
                replay = input().strip().lower()  
                if replay == "yes" or replay == "y":
                    break  
                elif replay == "no" or replay == "n":
                    print("Thanks for playing! Goodbye!")
                    return  
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")


    play_game() 

