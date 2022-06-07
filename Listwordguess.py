#Elizabeth Nassi
#have user guess random flower from list
#pseudocode
#Make list of different flowers, Choose random flower off of list, Print instructions of game, Have user guess flower, If guess is correct, print congratulations, If guess is incorrect, print that they guessed incorrectly, Ask if still want to guess, If yes, loop, If no, give answer, Ask user if want to keep playing, If yes, Choose new random flower, loop, If no, Say bye, end
#make three different list game options, not just flower
import random
import os
#from traceback import print_stack
os.system("cls")
name= input("Hello! What is your name? ")
print("Nice to meet you,", name, "! Welcome to Guess the Word. 😊")
game = True
while game:
    gamec = True
    while gamec:
        print("Would you like to play guess, 1, the animal, 2, the dessert, or 3, the flower?")
        choice= input("Please write your choice as a 1, 2, or 3. ")
        try:
            choice=int(choice)
            if choice>0 and choice<4:
                gamec = False
            else:
                print("I said, give me a 1, 2, or 3.")
        except:
            print("Sorry, that's not even a number. Please type a 1, 2, or 3.")
    if choice == 1:
        os.system("cls")
        print('*🐶🐱🐷🐰Guess the animal!!!🐸🐻🦊🐵*')
        print("**Make sure that your answers aren't capitalized!**")
        animallist = ["cat", "dog", "owl", "monkey", "snake", "pig", "bear", "koala", "panda", "fish", "rabbit", "horse", "bird", "turkey", "cow", "lizard"]
        animal = random.choice(animallist)
        animalplay = True
        while animalplay:
            if animal == "cat":
                print("Hint: This animal is often kept as a pet.")
            if animal == "dog":
                print("Hint: This animal is man's best friend.")
            if animal == "owl":
                print(":Hint: This animal is a symbol of wisdom.")
            if animal == "monkey":
                print("Hint: This animal likes bananas.")
            if animal == "snake":
                print("Hint: This animal has no legs.")
            if animal == "pig":
                print("Hint: This animal is often pink.")
            if animal == "bear":
                print("Hint: Winnie the Pooh.")
            if animal == "koala":
                print("Hint: This animal lives in Australia.")
            if animal == "panda":
                print("Hint: This animal is black and white.")
            if animal == "fish":
                print("Hint: This animal lives in water.")
            if animal == "rabbit":
                print("Hint: This animal often features in cliche magic shows.")
            if animal == "horse":
                print("Hint: This animal can be used for transportation.")
            if animal == "bird":
                print("Hint: This animal is four letters.")
            if animal ==  "turkey":
                print("Hint: Benjamin Franklin wanted this animal to be the country's national bird.")
            if animal == "cow":
                print("Hint: This animal is used for milk.")
            if animal == "lizard":
                print("Hint: This animal is a reptile.")
            guess = input("Your guess is...? 🤔 ")
            if guess in animal:
                print("🐶🐱🐷🐰 CONGRATULATIONS, " , name, "!!! You guessed correctly. 😀 🐸🐻🦊🐵")
                aplay = input("Want to play the animal game again? 🐾 Answer yes or no. ")
                if aplay == "no":
                    print("ok bye 👋")
                    animalplay = False
                    agame = input("Want to play a different game? Answer yes or no. ")
                    if agame == "no":
                        game = False
                if aplay == "yes":
                    animal = random.choice(animallist)
            else:
                print("Sorry, that's not correct. 🙁")
                aans = input("Want to guess again? Answer yes or no. ")
                if aans == "no":
                    print ("The animal was ", animal)
                    aplay = input("Want to play the animal game again? 🐾 Answer yes or no. ")
                    if aplay == "no":
                        print("ok bye 👋")
                        animalplay = False
                        agame = input("Want to play a different game? Answer yes or no. ")
                        if agame == "no":
                            print("Bye Bye")
                            game = False
                    if aplay == "yes":
                        animal = random.choice(animallist)
    if choice == 2:
        os.system("cls")
        print('*🍧🍦🥧🍨Guess the dessert!!!🍫🍰🧁🍪*')
        print("**Make sure that your answers aren't capitalized!**")
        dessertlist = ["icecream", "cake", "pie", "candy", "chocolate", "pudding", "cheesecake", "brownie", "cobbler", "cupcake", "tiramisu"]
        dessert = random.choice(dessertlist)
        dessertplay = True
        while dessertplay:
            if dessert == "icecream":
                print("Hint: This dessert is carried by some trucks.")
            if dessert == "cake":
                print("Hint: This dessert is often used to celebrate birthdays.")
            if dessert == "pie":
                print("Hint: 3.14.")
            if dessert == "candy":
                print("Hint: Don't take this dessert from strangers.")
            if dessert == "chocolate":
                print("Hint: This dessert is made using beans.")
            if dessert == "pudding":
                print("Hint: This dessert has seven letters.")
            if dessert == "cheesecake":
                print("Hint: This dessert has two words in it.")
            if dessert == "brownie":
                print("Hint: This dessert has it's color in it's name.")
            if dessert == "cobbler":
                print("Hint: This dessert starts with the letter c.")
            if dessert == "cupcake":
                print("Hint: This dessert is a smaller version of another dessert.")
            if dessert == "tiramisu":
                print("Hint: This dessert is coffee flavored.")
            guess = input("Your guess is...? 🤔 ")
            if guess in dessert:
                print("🍧🍦🥧🍨 CONGRATULATIONS, " , name, "!!! You guessed correctly. 😀 🍫🍰🧁🍪")
                dplay = input("Want to play the dessert game again? 🧁 Answer yes or no. ")
                if dplay == "no":
                    print("ok bye 👋")
                    dessertplay = False
                    dgame =  input("Want to play a different game? Answer yes or no. ")
                    if dgame == "no":
                        print("Bye Bye")
                        game = False
                if dplay == "yes":
                    dessert = random.choice(dessertlist)
            else:
                print("Sorry, that's not correct. 🙁")
                dans = input("Want to guess again? Answer yes or no. ")
                if dans == "no":
                    print ("The dessert was ", dessert)
                    dplay = input("Want to play the dessert game again? 🧁 Answer yes or no. ")
                    if dplay == "no":
                        print("ok bye 👋")
                        dessertplay = False
                        dgame =  input("Want to play a different game? Answer yes or no. ")
                        if dgame == "no":
                            print("Bye Bye")
                            game = False
                    if dplay == "yes":
                        dessert = random.choice(dessertlist)
    if choice == 3:
        os.system("cls")
        print('*🌸🌹🌺🌻Guess the flower!!!🌼🌷🥀💐*')
        print("**Make sure that your answers aren't capitalized!**")
        flowerlist = ["tulip", "lilac", "sunflower", "daisy", "hibiscus", "rose", "hydrangea", "lily", "iris", "hyacinth", "daffodil", "lavendar", "poppy", "peony"]
        flower = random.choice(flowerlist)
        flowerplay = True
        while flowerplay:
            if flower == "tulip":
                print("Hint: Netherlands is the greatest exporter of this flower.")
            if flower == "lilac":
                print("Hint: This flower is in the same family of the olive tree.")
            if flower == "sunflower":
                print("Hint: This flower has the name of a star in it's name.")
            if flower == "daisy":
                print("Hint: This flower symbolizes innocence.")
            if flower == "hibiscus":
                print("Hint: This flower thrives in warm temperatures.")
            if flower == "rose":
                print("Hint: This flower is the U.S. national flower.")
            if flower == "hydrangea":
                print("Hint: This flower is poisonous.")
            if flower == "lily":
                print("Hint: This flower is poisonous for cats.")
            if flower == "iris":
                print("Hint: This flower is also the name of the Greek goddess of rainbows and messages.")
            if flower == "hyacinth":
                print("Hint: In Greek mythology, Apollo turned his lover into this flower.")
            if flower == "daffodil":
                print("Hint: This flower is also known as narcissus.")
            if flower == "lavendar":
                print("Hint: This flower's scent is often used for relaxation.")
            if flower == "poppy":
                print("Hint: This flower is also the name of a type of seed placed on bagels.")
            if flower == "peony":
                print("This flower symbolizes good fortune and happy marriage.")
            guess = input("Your guess is...? 🤔 ")
            if guess in flower:
                print("🌼🌷🥀💐 CONGRATULATIONS, " , name, "!!! You guessed correctly. 😀 🌸🌹🌺🌻")
                play = input("Want to play the flower game again? 💐 Answer yes or no. ")
                if play == "no":
                    print("ok bye 👋")
                    flowerplay = False
                    fgame =  input("Want to play a different game? Answer yes or no. ")
                    if fgame == "no":
                        print("Bye Bye")
                        game = False
                if play == "yes":
                    flower = random.choice(flowerlist)
            else:
                print("Sorry, that's not correct. 🙁")
                ans = input("Want to guess again? Answer yes or no. ")
                if ans == "no":
                    print ("The flower was ", flower)
                    play = input("Want to play the flower game again? 💐 Answer yes or no. ")
                    if play == "no":
                        print("ok bye 👋")
                        flowerplay = False
                        fgame =  input("Want to play a different game? Answer yes or no. ")
                        if fgame == "no":
                            print("Bye Bye")
                            game = False
                    if play == "yes":
                        flower = random.choice(flowerlist)