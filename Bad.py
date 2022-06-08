#Elizabeth Nassi
#have user guess random flower from list
#pseudocode
#Make list of different flowers, Choose random flower off of list, Print instructions of game, Have user guess flower, If guess is correct, print congratulations, If guess is incorrect, print that they guessed incorrectly, Ask if still want to guess, If yes, loop, If no, give answer, Ask user if want to keep playing, If yes, Choose new random flower, loop, If no, Say bye, end
#make three different list game options, not just flower
#add score

import random
import os
os.system("cls")
name= input("Hello! What is your name? ")
print("Nice to meet you,", name, "! Welcome to Guess the Word. 😊")
input("Press enter to see your options.")
game = True
while game:
    gamec = True
    while gamec:
        os.system("cls")
        print("Would you like to 1) guess the animal, 2) guess the dessert, 3) guess the flower, or 4)leave the game entirely?")
        choice= input("Please write your choice as a 1, 2, 3, or 4. ")
        try:
            choice=int(choice)
            if choice>0 and choice<5:
                gamec = False
                if choice == 5:
                    print("Ok, Bye Bye! 👋")
                    game=False
            else:
                print("I said, give me a 1, 2, 3, or 4.")
        except:
            print("Sorry, that's not even a number. Please type a 1, 2, 3, or 4.")
    if choice == 4:
        game = False
    animallist = ["cat", "dog", "owl", "monkey", "snake", "pig", "bear", "koala", "panda", "fish", "rabbit", "horse", "bird", "turkey", "cow", "lizard"]
    dessertlist = ["icecream", "cake", "pie", "candy", "chocolate", "pudding", "cheesecake", "brownie", "cobbler", "cupcake", "tiramisu"]
    flowerlist = ["tulip", "lilac", "sunflower", "daisy", "hibiscus", "rose", "hydrangea", "lily", "iris", "hyacinth", "daffodil", "lavendar", "poppy", "peony"]
    animaldict = {"cat":"Hint: This animal is often kept as a pet.", "dog":"Hint: This animal is man's best friend.", "owl":"Hint: This animal is a symbol of wisdom.", "monkey":"Hint: This animal likes bananas.", "snake":"Hint: This animal has no legs.", "pig":"Hint: This animal is often pink.", "bear":"Hint: Winnie the Pooh.", "koala":"Hint: This animal lives in Australia.", "panda":"Hint: This animal is black and white.", "fish":"Hint: This animal lives in water.", "rabbit":"Hint: This animal often features in cliche magic shows.", "horse":"Hint: This animal can be used for transportation.", "bird":"Hint: This animal is four letters.", "turkey":"Hint: Benjamin Franklin wanted this animal to be the country's national bird.", "cow":"Hint: This animal is used for milk.", "lizard":"Hint: This animal is a reptile."}
    dessertdict = {"icecream":"Hint: This dessert is carried by some trucks.", "cake":"Hint: This dessert is often used to celebrate birthdays.", "pie":"Hint: 3.14.", "candy":"Hint: Don't take this dessert from strangers.", "chocolate":"Hint: This dessert is made using beans.", "pudding":"Hint: This dessert has seven letters.", "cheesecake":"Hint: This dessert has two words in it.", "brownie":"Hint: This dessert has it's color in it's name.", "cobbler":"Hint: This dessert starts with the letter c.", "cupcake":"Hint: This dessert is a smaller version of another dessert.", "tiramisu":"Hint: This dessert is coffee flavored."}
    flowerdict = {"tulip":"Hint: Netherlands is the greatest exporter of this flower.", "lilac":"Hint: This flower is in the same family of the olive tree.", "sunflower":"Hint: This flower has the name of a star in it's name.", "daisy":"Hint: This flower symbolizes innocence.", "hibiscus":"Hint: This flower thrives in warm temperatures.", "rose":"Hint: This flower is the U.S. national flower.", "hydrangea":"Hint: This flower is poisonous.", "lily":"Hint: This flower is poisonous for cats.", "iris":"Hint: This flower is also the name of the Greek goddess of rainbows and messages.", "hyacinth":"Hint: In Greek mythology, Apollo turned his lover into this flower.", "daffodil":"Hint: This flower is also known as narcissus.", "lavendar":"Hint: This flower's scent is often used for relaxation.", "poppy":"Hint: This flower is also the name of a type of seed placed on bagels.", "peony":"Hint: this flower symbolizes good fortune and happy marriage."}
    if choice == 1:
        emoji1="🐶🐱🐷🐰"
        emoji2="🐸🐻🦊🐵"
        y = animallist
        x = animaldict
        option = "animal 🐾"
    if choice == 2:
        emoji1="🍧🍦🥧🍨"
        emoji2="🍫🍰🧁🍪"
        y = dessertlist
        x = dessertdict
        option = "dessert 🧁"
    if choice == 3:
        emoji1="🌸🌹🌺🌻"
        emoji2="🌼🌷🥀💐"
        y = flowerlist
        x = flowerdict
        option = "flower 💐"
    z="That's not even a word. Answer yes or no."
    t="I said answer yes or no."
    play = True
    while play:
        os.system("cls")
        word = random.choice(y)
        print(emoji1, "Guess the " ,option, "!!!", emoji2)
        print("**Make sure that your answers aren't capitalized!**")
        print(x[word])
        guessgo = True
        while guessgo:
            guess = input("Your guess is...? 🤔 ")
            if guess in word:
                print(emoji1, "CONGRATULATIONS, " , name, "!!! You guessed correctly.", emoji2)
                guessgo = False
            else:
                print("Sorry, that's not correct. 🙁")
                mess = True
                while mess:
                    ans = input("Want to guess again? Answer yes or no. ")
                    try:
                        ans=str(ans)
                        if ans == "no" or "yes":
                            mess = False
                            if ans == "no":
                                print ("The " ,option, " was ", word)
                                guessgo = False
                        else:
                            print(t)
                    except:
                        print(z)
        mess2 = True
        while mess2:
                iplay = input("Want to play the " ,option, " game again? Answer yes or no. ")
                try:
                    iplay=str(iplay)
                    if iplay == "no" or "yes":
                        mess2 = False
                        if ans == "no":
                            print ("Ok thanks for playing. 👋")
                            play = False
                    else:
                        print(t)
                except:
                    print(z)