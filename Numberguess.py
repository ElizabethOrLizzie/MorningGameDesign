#Elizabeth Nassi
#Input user’s name,Input menu choice(1 Instruction, 2 level 1: 1-25, 3 Level 2: 1 – 50, 4 Level 3: 1-100, 5 Print score, 6 Exit)If user choose 1:, Print instructions, Input enter to go back to main menu, If user choose 2:, Print “pick a number 1-25”, Pick a random number 1-25, While loop:, Input ”your guess is”, If guess = number:, Print ”Congratulations”, Send user to menu, If guess less than number, Print”number is bigger”, If guess more than number, Print”number is smaller”, If user choose 3:, Replace1-25 with 1-50, If user choose 4:, Replace 1-25 with 1-100, If user choose 5:, print scoreIf user choose 6:, End game
import random
import os, datetime
os.system("cls")
name = input("Hello there! What is your name? ")
print("Nice to meet you," ,name,".")
input("Press enter to go to the main menu. ")
game = True
while game:
    os.system("cls")
    print("Menu:")
    print("____")
    print("Would you like to go to 1) instructions, 2) level 1: guess a number from 1-25, 3) level 2: guess a number from 1-50, 4) level 3: guess a number from 1-100, 5) print the scoreboard, or 6) exit the game entirely.")
    stupid = True
    while stupid:
        choice = input("Answer as a 1, 2, 3, 4, 5, or 6. ")
        try:
            choice=int(choice)
            if choice>0 and choice<7:
                stupid = False
            else:
                print("Your choice must be from 1-6.")
        except:
            print("That's not a number. Your choice has to be a number from 1-6.")
    if choice == 6:
        print("Ok, bye then. 👋")
        game = False
    if choice == 1:
        os.system("cls")
        print("Welcome to the game, guess the number," ,name,".")
        print("There are three possible levels to choose from. You can guess a number from 1-25, 1-50, or 1-100.")
        print("Playing at higher levels and guessing the number in less guesses raises your score.")
        print("After each guess, you will be told whether the number is larger or smaller than your guess.")
        print("Remember to press enter after typing in your answer to submit it.")
        print("Good luck!")
        input("Press enter to go back to the main menu. ")
    if choice == 2:
        max = 25
    if choice == 3:
        max = 50
    if choice == 4:
        max = 100
    if choice>1 and choice<5:
        os.system("cls")
        level = choice - 1
        print("Level", level,": guess a number from 1-",max,".")
        num = random.randint(1,max)
        count = 0
        stay = True
        while stay and count < max:
            guess = input("Your guess is: ")
            try:
                guess=int(guess)
                if guess>0 and guess<max+1:
                    if guess>num:
                        print("The number is smaller than",guess,".")
                    if guess<num:
                        print("The number is bigger than",guess,".")
                    if guess==num:
                        print("🏆🎉CONGRATULATIONS,",name,"!🎉🏆 You guessed the number.")
                        score = max - count
                        print(name,", your score is",score)
                        input("Press enter to move on. ")
                        stay = False
                else:
                    print("That number isn't even between 1 and",max)
            except:
                print("That's not even a number! You're supposed to guess a number between 1 and",max)
            count += 1
        if count == max:
            print("Wow, I gave you as many tries as there were possible numbers and you STILL couldn't guess the number. You're really bad at this.")
            score = max - count
            print(name,", your score is",score)
            input("Press enter to move on. In the program. Not sure if you can move on from how badly you failed emotionally.")
    if choice == 5:
        high = 0
        if score>high:
            high = score
        two = 0
        if score>two and score<high:
            two = score
        three = 0
        if score>three and score<two:
            three = score
        four = 0
        if score>four and score<three:
            four = score
        five = 0
        if score>five and score<four:
            five = score
        date=datetime.datetime.now()
        scrLine=str(high)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
        scrLine2=str(two)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
        scrLine3=str(three)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"       
        scrLine4=str(four)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
        scrLine5=str(five)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
        myFile = open("scre.txt", 'w')
        myFile.write(scrLine+scrLine2+scrLine3+scrLine4+scrLine5)
        myFile.close()