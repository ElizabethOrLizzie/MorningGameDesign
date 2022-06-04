#Elizabeth Nassi
#have user guess random flower from list
#pseudocode
#Make list of different flowers, Choose random flower off of list, Print instructions of game, Have user guess flower, If guess is correct, print congratulations, If guess is incorrect, print that they guessed incorrectly, Ask if still want to guess, If yes, loop, If no, give answer, Ask user if want to keep playing, If yes, Choose new random flower, loop, If no, Say bye, end

import random
import os
os.system("cls")
print('*🌸🌹🌺🌻Guess the flower!!!🌼🌷🥀💐*')
print("**Make sure that your answers aren't capitalized!**")
list = ["tulip", "lilac", "sunflower", "daisy", "hibiscus", "rose", "hydrangea", "lily", "iris", "hyacinth", "daffodil", "lavendar", "poppy", "peony"]
flower = random.choice(list)
while True:
    guess = input("Your guess is...? 🤔 ")
    if guess in flower:
        print("🌼🌷🥀💐 CONGRATULATIONS!!! You guessed correctly. 😀 🌸🌹🌺🌻")
        play = input("Want to play again? 💐 ")
        if play == "no":
            print("ok bye 👋")
            break
        if play == "yes":
           flower = random.choice(list)
    else:
        print("Sorry, that's not correct. 🙁")
        ans = input("Want to guess again? Answer yes or no. ")
        if ans == "no":
            print ("The flower was ", flower)
            play = input("Want to play again? 💐 Answer yes or no. ")
            if play == "no":
                print("ok bye 👋")
                break
            if play == "yes":
                flower = random.choice(list)