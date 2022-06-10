#Elizabeth Nassi
#first let's import random procedures since we will be shuffling
import random, os
os.system('cls')
deck=[]
#next, let's start building list holders so we can place our cards in there:
def create_DECK():
    global deck
    numberCards = []
    suits = ["♥️","♦️", "♣️", "♠️"]
    royals = ["J", "Q", "K", "A"]
    

    #now, let's start using loops to add our content:
    for i in range(2,11):
        numberCards.append(str(i))
        #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
        #this will add the royal faces to the cardbase

    
    for k in range(4):
        for l in range(13):
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make

    #now let's see the cards!
    counter=0
    for row in range(4):
        for col in range(13):
            print(deck[counter], end=" ")
            counter +=1
        print()
    #now let's shuffle our deck!
def deal():
    global player1card
    global player2card
    random.shuffle(deck)
    player1card=[]
    player2card=[]
    for l in range(52):
        if l%2==0:
            player1card.append(deck[l])
        else:
            player2card.append(deck[l])
    #I also want to see what the deck looks like before shuffling. We should have
        #done that a while ago... oh well!
create_DECK()
deal()

game = True
while game:
    os.system("cls")
    print("Welcome to War!")
    print('''main menu:
    1) instructions 
    2) start a new game
    3) leave game''')
    stupid = True
    while stupid:
        choice = input("Please enter your choice as a 1, 2, or 3. ")
        try:
            choice=int(choice)
            if choice>0 and choice<4:
                stupid = False
            else:
                print("Your choice must be from 1-3.")
        except:
            print("That's not a number. Your choice has to be a number from 1-3.")
    if choice == 1:
        os.system("cls")
        print("Welcome to the game War.")
        print("If you have ever played the card game war before, this game is essentially just that.")
        print("The objective of the game is to get the most cards.")
        print("A deck of cards is shuffled and split evenly between two players.")
        print("The two players' decks are placed upside down.")
        print("The players are unable to see their own cards, or their opponent's.")
        print("Both players simultaneously reveal the top card of their deck. This is called a battle.")
        print("If your card is larger than your opponent's, you get to keep both your card and your opponent's at the bottom of your deck.")
        print("The same thing applies if your opponent has a larger card than you; they get to keep both cards.")
        print("On the rare occasion that both players have the same top card, the next top card is drawn to see who gets to claim both the new and previous top cards.")
        print("From then on, battles determine who gets to keep the top 2 cards instead of 1, raising the stakes for the rest of the game.")
        print("The game ends if someone receives all of the cards, or after 50 battles.")
        print("A (Ace) is worth 1, J (Jack) is worth 11, Q (Queen) is worth 12, and K (King) is worth 13.")
        print("Good luck, and have fun. 😊")
        input("Press enter to return to the main menu. ")
#change if someone has 0 cards to if someone has 52 cards
    if choice == 3:
        print("Ok, bye! 👋")
        game = False
    if choice == 2:
        os.system("cls")
        carddict = {
            "A ♥️": 1,
            "2 ♥️": 2,
            "3 ♥️": 3,
            "4 ♥️": 4,
            "5 ♥️": 5,
            "6 ♥️": 6,
            "7 ♥️": 7,
            "8 ♥️": 8,
            "9 ♥️": 9,
            "10 ♥️": 10,
            "J ♥️": 11,
            "Q ♥️": 12,
            "K ♥️": 13,
            "A ♦️": 1,
            "2 ♦️": 2,
            "3 ♦️": 3,
            "4 ♦️": 4,
            "5 ♦️": 5,
            "6 ♦️": 6,
            "7 ♦️": 7,
            "8 ♦️": 8,
            "9 ♦️": 9,
            "10 ♦️": 10,
            "J ♦️": 11,
            "Q ♦️": 12,
            "K ♦️": 13,
            "A ♣️": 1,
            "2 ♣️": 2,
            "3 ♣️": 3,
            "4 ♣️": 4,
            "5 ♣️": 5,
            "6 ♣️": 6,
            "7 ♣️": 7,
            "8 ♣️": 8,
            "9 ♣️": 9,
            "10 ♣️": 10,
            "J ♣️": 11,
            "Q ♣️": 12,
            "K ♣️": 13,
            "A ♠️": 1,
            "2 ♠️": 2,
            "3 ♠️": 3,
            "4 ♠️": 4,
            "5 ♠️": 5,
            "6 ♠️": 6,
            "7 ♠️": 7,
            "8 ♠️": 8,
            "9 ♠️": 9,
            "10 ♠️": 10,
            "J ♠️": 11,
            "Q ♠️": 12,
            "K ♠️": 13
        }
        player1 = input("Player 1's name: ")
        player2 = input("Player 2's name: ")
        deal()
        cnt = 0
        play = True
        z = 0
        while play and cnt<50:
            input("press enter to battle")
            topcard1 = carddict[player1card[z]]
            topcard2 = carddict[player2card[z]]
            print(player1,"'s top card is", player1card[z], "and", player2,"'s top card is", player2card[z])
            #need to assign values to cards- computer dont know how much diamond king worth etc.
            if topcard1>topcard2:
                w = player1
                wcard = player1card
                l = player2
                lcard = player2card
            if topcard2>topcard1:
                w = player2
                wcard = player2card
                l = player1
                lcard = player1card
            if topcard1 != topcard2:
                print(w, "won the battle.")
                wcard.extend(lcard[0:z+1])
                lcard[0:z+1] = []
                wcard.extend(wcard[0:z+1])
                wcard[0:z+1] = []
                print(player1,"has", len(player1card), "cards and", player2, "has", len(player2card), "cards.")
                print("")
                cnt+=1
                if len(wcard)==52:
                    print("Game over:", w, "has all of the cards.")
                    play = False
            else:
                z+=1
                print("Both cards are equal!")
                print("Battle again for both these cards, and new ones.")
        if cnt >= 50:
            print("Game over: you’ve used your 50 battles.")
        if len(player1card)>len(player2card):
            winner = player1
        if len(player1card)<len(player2card):
            winner = player2
        print("🎉Congratulations,", winner, "you win!🎉")
        input("press enter to return to the main menu ")