# -*- coding: utf-8 -*-
"""
Project #3 Assigment

11/14/2020
"""
from random import shuffle, choice
from time import sleep

P = input('Enter players name: ')

#Creation of the deck
def createDeck ():
    Deck = []
    for i in range (4):
        for card in range (2,11):
            Deck.append(str(card))
        for card in ['J', 'Q', 'K', 'A']:
            Deck.append(card)
    shuffle(Deck)
    return Deck
cardDeck = createDeck()

#Player Class
class Player:
    def __init__(self, hand=[]):
        self.hand = hand
        self.score = 0
        self.score = self.setScore()
        
    def __str__(self):
        currentHand = ''
        for card in self.hand:
            currentHand += str(card) + ' '
        self.score = self.setScore()
        finalStatus = str(currentHand) + '  score: ' + str(self.score)
        return finalStatus
    
    def setScore(self):
        handDic = {}
        for card in self.hand:
            if card in handDic:
                handDic[card] += 1
            else: 
                handDic[card] = 1
        for card in handDic:
            if handDic[card] == 4:
                self.score +=1
                self.hand.remove(card)
                self.hand.remove(card)
                self.hand.remove(card)
                self.hand.remove(card)
        return self.score
    
    def hit (self,card):
        self.hand.append(card)
        self.score = self.setScore()
        
    def end (self):
        return (str(self.score))
        
                 

playerHand = [cardDeck.pop(),cardDeck.pop(),cardDeck.pop(),cardDeck.pop(),cardDeck.pop()]
bootHand = [cardDeck.pop(),cardDeck.pop(),cardDeck.pop(),cardDeck.pop(),cardDeck.pop()]
P1 = Player(playerHand)
Boot = Player(bootHand)
  
#Game initalization    
while len(cardDeck) > 0:
    print(len(cardDeck),'cards left in the deck pile')
    print(P + ' your current hand is:')
    print (P1)
    # print (Boot)
    Card = input(P + ' enter the card you want to ask for: ')
    
    while Card == '--help':
        print(chr(27) + "[2J")
        print('The goal is to win the most "books" of cards. A book is any four of a kind, such as four kings, four aces, and so on.')
        print('The player to the left of the dealer looks directly at any opponent and says, for example, "Give me your kings," usually addressing the opponent by name and specifying the rank that they want, from ace down to two. The player who is "fishing “must have at least one card of the rank that was asked for in their hand. The player who is addressed must hand over all the cards requested. If the player has none, they say, "Go fish!" and the player who made the request draws the top card of the stock and places it in their hand.')
        sleep(10)
        resume = input('Type --resume to continue: ')
        if resume == '--resume':
            break
        else:
            Card == '--help'

    if Card in P1.hand and Card in Boot.hand:
         for i in Boot.hand:
             if i == Card:
                 P1.hand.append(i)
                 Boot.hand.remove(i)
    else:
        P1.hit(cardDeck.pop())
    print (P1)
    print('Now its the PCs turn')
    Card = choice(Boot.hand)
    print ('PC asked for a', Card)
    print('\n')
    # sleep(5)
    if Card in P1.hand and Card in Boot.hand:
         for i in P1.hand:
             if i == Card:
                 Boot.hand.append(i)
                 P1.hand.remove(i)
    else:
        Boot.hit(cardDeck.pop())    

if P1.score >= Boot.score:
    print (P, 'has won the game')
else:
    print (P, 'lost against the PC')

print(P ,' scored:' , P1.end())
print('Boot scored: ' + Boot.end())
