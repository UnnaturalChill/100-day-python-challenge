print(" Fake fan finder")
print("-----------------")

print()

favouriteGame = input("What's your favourite game series? >\033[34m ")

if favouriteGame == "Touhou":
    favouriteCharacter = input("\033[0mAlright, very good! But who's your favourite character? >\033[34m ")

    if favouriteCharacter == "Cirno":
        favouriteThingToDo = input("\033[0mOkay well, you don't even have to play the game to know her! What does she like to do on her free time? >\033[34m ")

        if favouriteThingToDo == "Freeze frogs":
            bestFriend = input("\033[0mEhhh?? How do you know that?? Uhhh, who's her best friend? >\033[34m  ")

            if bestFriend == "Daiyousei":
                print("\033[0mYou truly are a Touhou fan, you know everything about her. Good job!")

            elif bestFriend == "Me":
                print("No you silly, she is not your best friend. She is MY best friend!!!")
                
            else: print("\033[0mNope, try again!")
        else: print("\033[0mWrong! That's not what she does!")
    else: print("\033[0mAre you saying that Cirno isn't your favourite character?! Try again!")
else: print("\033[0mAre you saying Touhou isn't your favourite game series?! Try again!")