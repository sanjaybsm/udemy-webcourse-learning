#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    l = []

    def __init__(self):
        for i in range(len(SUITE)):
            for j in range(len(RANKS)):
                Deck.l.append(SUITE[i]+RANKS[j])

        Deck.l.extend(RANKS)

    def __str__(self):
        return "values of deck ss "

    def return_deck(self):
        return Deck.l

    def shuffle_deck(self):
        shuffle(Deck.l)
        return Deck.l

    def split_list(self):
        half = len(Deck.l)//2
        return Deck.l[:half], Deck.l[half:]

s = Deck()
print(s.return_deck())
print(s.shuffle_deck())
x, y = s.split_list()
print(x)
print(y)

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def add_card(self):
        print('method to add card')

    def remove_card(self):
        print('remove card from hand')

class Player():
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    hand = ''
    def __init__(self):
        Player.hand = Hand()
        Player.hand.add_card()


p = Player()

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
