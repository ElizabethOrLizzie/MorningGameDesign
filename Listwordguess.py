#Elizabeth Nassi
#have user guess random flower from list
#pseudocode
#Make list of different flowers, Choose random flower off of list, Print instructions of game, Have user guess flower, If guess is correct, print congratulations, If guess is incorrect, print that they guessed incorrectly, Ask if still want to guess, If yes, loop, If no, give answer, Ask user if want to keep playing, If yes, Choose new random flower, loop, If no, Say bye, end
#make three different list game options, not just flower
import random
import os, datetime
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
        cnt = 0
        os.system("cls")
        print('*🐶🐱🐷🐰Guess the animal!!!🐸🐻🦊🐵*')
        print("**Make sure that your answers aren't capitalized!**")
        animallist = ["cat", "dog", "owl", "monkey", "snake", "pig", "bear", "koala", "panda", "fish", "rabbit", "horse", "bird", "turkey", "cow", "lizard"]
        animaldict = {"cat":"Hint: This animal is often kept as a pet.", "dog":"Hint: This animal is man's best friend.", "owl":"Hint: This animal is a symbol of wisdom.", "monkey":"Hint: This animal likes bananas.", "snake":"Hint: This animal has no legs.", "pig":"Hint: This animal is often pink.", "bear":"Hint: Winnie the Pooh.", "koala":"Hint: This animal lives in Australia.", "panda":"Hint: This animal is black and white.", "fish":"Hint: This animal lives in water.", "rabbit":"Hint: This animal often features in cliche magic shows.", "horse":"Hint: This animal can be used for transportation.", "bird":"Hint: This animal is four letters.", "turkey":"Hint: Benjamin Franklin wanted this animal to be the country's national bird.", "cow":"Hint: This animal is used for milk.", "lizard":"Hint: This animal is a reptile."}
        animal = random.choice(animallist)
        animalplay = True
        while animalplay:
            print(animaldict[animal])
            guess = input("Your guess is...? 🤔 ")
            cnt+=1
            if guess in animal:
                score = 50 - cnt
                print("🐶🐱🐷🐰 CONGRATULATIONS, " , name, "!!! You guessed correctly. 😀 🐸🐻🦊🐵")
                print("Your score is",score)
                high = 0
                if score>high:
                    high = score
                date=datetime.datetime.now()
                scrLine=str(high)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
                myFile = open("scre1.txt", 'w')
                myFile.write(scrLine)
                myFile.close()
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
        cnt = 0
        os.system("cls")
        print('*🍧🍦🥧🍨Guess the dessert!!!🍫🍰🧁🍪*')
        print("**Make sure that your answers aren't capitalized!**")
        dessertlist = ["icecream", "cake", "pie", "candy", "chocolate", "pudding", "cheesecake", "brownie", "cobbler", "cupcake", "tiramisu"]
        dessertdict = {"icecream":"Hint: This dessert is carried by some trucks.", "cake":"Hint: This dessert is often used to celebrate birthdays.", "pie":"Hint: 3.14.", "candy":"Hint: Don't take this dessert from strangers.", "chocolate":"Hint: This dessert is made using beans.", "pudding":"Hint: This dessert has seven letters.", "cheesecake":"Hint: This dessert has two words in it.", "brownie":"Hint: This dessert has it's color in it's name.", "cobbler":"Hint: This dessert starts with the letter c.", "cupcake":"Hint: This dessert is a smaller version of another dessert.", "tiramisu":"Hint: This dessert is coffee flavored."}
        dessert = random.choice(dessertlist)
        dessertplay = True
        while dessertplay:
            print(dessertdict[dessert])
            guess = input("Your guess is...? 🤔 ")
            cnt+=1
            if guess in dessert:
                score = 50 - cnt
                print("🍧🍦🥧🍨 CONGRATULATIONS, " , name, "!!! You guessed correctly. 😀 🍫🍰🧁🍪")
                print("Your score is",score)
                high = 0
                if score>high:
                    high = score
                date=datetime.datetime.now()
                scrLine=str(high)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
                myFile = open("scre1.txt", 'w')
                myFile.write(scrLine)
                myFile.close()
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
        cnt = 0
        os.system("cls")
        print('*🌸🌹🌺🌻Guess the flower!!!🌼🌷🥀💐*')
        print("**Make sure that your answers aren't capitalized!**")
        flowerlist = ["tulip", "lilac", "sunflower", "daisy", "hibiscus", "rose", "hydrangea", "lily", "iris", "hyacinth", "daffodil", "lavendar", "poppy", "peony"]
        flowerdict = {"tulip":"Hint: Netherlands is the greatest exporter of this flower.", "lilac":"Hint: This flower is in the same family of the olive tree.", "sunflower":"Hint: This flower has the name of a star in it's name.", "daisy":"Hint: This flower symbolizes innocence.", "hibiscus":"Hint: This flower thrives in warm temperatures.", "rose":"Hint: This flower is the U.S. national flower.", "hydrangea":"Hint: This flower is poisonous.", "lily":"Hint: This flower is poisonous for cats.", "iris":"Hint: This flower is also the name of the Greek goddess of rainbows and messages.", "hyacinth":"Hint: In Greek mythology, Apollo turned his lover into this flower.", "daffodil":"Hint: This flower is also known as narcissus.", "lavendar":"Hint: This flower's scent is often used for relaxation.", "poppy":"Hint: This flower is also the name of a type of seed placed on bagels.", "peony":"Hint: this flower symbolizes good fortune and happy marriage."}
        flower = random.choice(flowerlist)
        flowerplay = True
        while flowerplay:
            print(flowerdict[flower])
            guess = input("Your guess is...? 🤔 ")
            cnt+=1
            if guess in flower:
                score = 50 - cnt
                print("🌼🌷🥀💐 CONGRATULATIONS, " , name, "!!! You guessed correctly. 😀 🌸🌹🌺🌻")
                print("Your score is",score)
                high = 0
                if score>high:
                    high = score
                date=datetime.datetime.now()
                scrLine=str(high)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
                myFile = open("scre1.txt", 'w')
                myFile.write(scrLine)
                myFile.close()
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