import random


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        if suit == "hearts" or suit == "diamonds":
            self.color = "red"

        if suit == "spades" or suit == "clubs":
            self.color = "black"
    def print(self):
        print(str(self.number) + " of " + str(self.suit))



class Deck:
    def __init__(self):
        self.cards = []
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
                self.cards.append(Card(s, v))

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            # gen random int
            r = random.randint(0, i)
            temp = self.cards[r]
            self.cards[r] = self.cards[i]
            self.cards[i] = temp
    def print(self):
        for card in self.cards:
            card.print()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.aces = 0
    def draw(self, deck):
        newCard = deck.cards.pop()
        self.hand.append(newCard)
        if newCard.number == "J" or newCard.number == "Q" or newCard.number == "K":
            self.score += 10
        elif newCard.number == "A":
            self.score += 11
            self.aces += 1
        else:
            self.score += newCard.number
    def print(self):
        print(str(self.name) + ", your hand is:")
        for card in self.hand:
            card.print()
hello = True
while hello == True:
    myDeck = Deck()
    myDeck.shuffle()
    playerName = input("What is your name? ")
    myPlayer = Player(playerName)
    myDealer = Player("King of the world")
    myPlayer.draw(myDeck)
    myPlayer.draw(myDeck)
    myDealer.draw(myDeck)
    myDealer.draw(myDeck)
    myPlayer.print()
    print(str(playerName) + ", your hand is: " + str(myPlayer.score))
    playing = True
    print("The King of the World's first card is:")
    myDealer.hand[0].print()


    while playing:
        player_action = input("Would you like to (h)it or (s)tand ")
        if player_action.lower() == "h":
            myPlayer.draw(myDeck)
            myPlayer.print()
            print("")
            if myPlayer.score >= 22:
                if myPlayer.aces >= 1:
                    myPlayer.score -= 10
                    myPlayer.aces -= 1
                else:
                    print("You failed to defeat the King of the World")
                    playing = False
            print(myPlayer.score)
        elif player_action.lower() == "s":
            playing = False
        else:
            print("Invalid command, type either h or s")



    print("The King of the Worlds hand and score are:")
    myDealer.print()
    print(myDealer.score)

    if myPlayer.score >= 22:
        print("You busted!!!")
    else:
        while myDealer.score <= 16 or myDealer.score < myPlayer.score:
            myDealer.draw(myDeck)
            if myDealer.score >= 22 and myDealer.aces >= 1:
                myDealer.score -= 10
                myDealer.aces -= 1
            myDealer.print()
            print("King of the World's score is:")
            print(myDealer.score)
        if myDealer.score >= 22 or myPlayer.score > myDealer.score:
            print("You win!!!")
        elif myPlayer.score == myDealer.score:
            print("You tied(barely)!")
        else:
            print("You lose(obviously)!")
    hi = True
    while hi == True:
        replay = input("Do you want to play again([y]es or [n]o)?")
        if replay.lower()[0] == "n":
            hello = False
            hi = False
        elif replay.lower()[0] != "y":
            print("Invalid. Please type Y or N")
        else:
            hi = False