def start():
    import random

    def __init__():
        print("This is Odd eve game")

    def toss():
        print("Choose Odd or Even for toss")
        user_choice = (input()).casefold()

        if user_choice == "odd":
            print("You choose Odd, so I choose even.")
        elif user_choice == "even" or user_choice == "eve":
            print("You choose even, so I choose odd")
        else:
            print("hello you were given two options and you choose to mess it up, well congrats! \nBye!")
            quit()

        print("Now Type any number from 1 to 10 (well ok how it goes so just do it :/ )")
        Done = False
        while not Done:
            try:
                toss_inp = int(input())
                if toss_inp <= 0 or toss_inp >= 11:
                    print("Maybe try again with a number within the given range?")
                else:
                    Done = True
            except:
                print("maybe try again with an actual number?")



        toss_comp_imp = random.randint(1,10)

        if (toss_comp_imp+toss_inp)%2 == 0:
            if user_choice == "even" or user_choice == "eve":
                print("Well, ", toss_inp, " + ", toss_comp_imp , " is ", (toss_comp_imp+toss_inp), " Which is even, So You win :)")
                player_toss_win()
            else:
                print("Well, ", toss_inp, " + ", toss_comp_imp , " is ", (toss_comp_imp+toss_inp), " Which is even, So I win :)")
                computer_toss_win()
        else:
            if user_choice == "odd":
                print("Well, ", toss_inp, " + ", toss_comp_imp , " is ", (toss_comp_imp+toss_inp), " Which is odd, So You win :)")
                player_toss_win()
            else:
                print("Well, ", toss_inp, " + ", toss_comp_imp , " is ", (toss_comp_imp+toss_inp), " Which is odd, So I win :)")
                computer_toss_win()

    def player_toss_win():
        print("What do you choose? Batting or Balling?")
        Done = False
        while not Done:
            plr_choice = (input()).casefold()
            if "bat" in plr_choice or "batting" in plr_choice:
                print("You Choose batting... I see...")
                Done = True
            elif "ball" in plr_choice or "balling" in plr_choice:
                print("You Choose Balling... I see...")
                Done = True
            else:
                print("OK, Try again... \nBatting Or Balling?")
        DaGame(plr_choice)

    def computer_toss_win():
        Options = ["batting","balling"]
        choice = random.choice(Options)
        print("I choose ", choice)
        if choice == "batting":
            DaGame("balling")
        else:
            DaGame("batting")

    def DaGame(choice):
        if "bat" in choice:
            print("Its your Batting, Type any number within Range 1-10")
            out = False
            score = 0
            while not out:
                try:
                    inp = int(input())
                    if inp <= 0 or inp >= 11:
                        print("Maybe try again with a number within the given range?")
                    else:
                        cmp_imp = random.randint(1,10)
                        print("You choose ", inp, " and I choose ", cmp_imp)
                        if inp-cmp_imp == 1 or cmp_imp-inp == 1 or (cmp_imp == 1 and inp == 10) or (inp == 1 and cmp_imp== 10):
                            print("OUT!")
                            out = True
                        elif inp == cmp_imp:
                            print("Squared!!!")
                            score += inp * cmp_imp
                        else:
                            score += inp
                        print("Total score = ", score)
                except:
                    print("maybe try again with an actual number?")

            print("Your score was ", score,"\n\n")

            print("Its my batting now\n")
            out = False
            cmpscore = 0
            while not out:
                try:
                    inp = int(input())
                    if inp <= 0 or inp >= 11:
                        print("Maybe try again with a number within the given range?")
                    else:
                        cmp_imp = random.randint(1,10)
                        print("You choose ", inp, " and I choose ", cmp_imp)
                        if inp-cmp_imp == 1 or cmp_imp-inp == 1 or (cmp_imp == 1 and inp == 10) or (inp == 1 and cmp_imp== 10):
                            print("OUT!")
                            out = True
                        elif inp == cmp_imp:
                            print("Squared!!!")
                            cmpscore += inp * cmp_imp
                        else:
                            cmpscore += cmp_imp
                        print("Total score = ", cmpscore)
                except:
                    print("maybe try again with an actual number?")

            print("My score was ", cmpscore, "and your score was ", score, "!\n")
            if score>cmpscore:
                print("YOU WIN!!!\n")
            elif score<cmpscore:
                print("YOU LOSE!!!\n")
            else:
                print("Tie :/")
        if "ball" in choice:
            print("Its my batting now\n")
            out = False
            cmpscore = 0
            while not out:
                try:
                    inp = int(input())
                    if inp <= 0 or inp >= 11:
                        print("Maybe try again with a number within the given range?")
                    else:
                        cmp_imp = random.randint(1,10)
                        print("You choose ", inp, " and I choose ", cmp_imp)
                        if inp-cmp_imp == 1 or cmp_imp-inp == 1 or (cmp_imp == 1 and inp == 10) or (inp == 1 and cmp_imp== 10):
                            print("OUT!")
                            out = True
                        elif inp == cmp_imp:
                            print("Squared!!!")
                            cmpscore += inp * cmp_imp
                        else:
                            cmpscore += cmp_imp
                        print("Total score = ", cmpscore)
                except:
                    print("maybe try again with an actual number?")

            print("My score was ", cmpscore, '\n\n')
            print("Its your batting now\n")

            out = False
            score = 0
            while not out:
                try:
                    inp = int(input())
                    if inp <= 0 or inp >= 11:
                        print("Maybe try again with a number within the given range?")
                    else:
                        cmp_imp = random.randint(1,10)
                        print("You choose ", inp, " and I choose ", cmp_imp)
                        if inp-cmp_imp == 1 or cmp_imp-inp == 1 or (cmp_imp == 1 and inp == 10) or (inp == 1 and cmp_imp== 10):
                            print("OUT!")
                            out = True
                        elif inp == cmp_imp:
                            print("Squared!!!")
                            score += inp * cmp_imp
                        else:
                            score += inp
                        print("Total score = ", score)
                except:
                    print("maybe try again with an actual number?")

            print("My score was ", cmpscore, "and your score was ", score, "!\n")
            if score>cmpscore:
                print("YOU WIN!!!\nGG")
            elif score<cmpscore:
                print("YOU LOSE!!!\n", "L"*100)
            else:
                print("Tie :/")



    __init__()
    toss()

