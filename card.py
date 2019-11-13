from random import shuffle

class Card:
    SUITS = ('♦', '♣', '♥', '♠')
    FACES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self, suit, face):
        if suit not in Card.SUITS:
            raise ValueError("Unknown suit")
        if face not in Card.FACES:
            raise ValueError("Unknown face")
        self.suit = suit
        self.face = face

    def value(self):
        if self.face[0].isdigit():
            return int(self.face)
        else:
            if self.face == 'A':
                return 11
            else:
                return 10
    
    def __str__(self):
        return self.suit + self.face

def gen_deck():
    deck = [Card(suit, face) for face in Card.FACES for suit in Card.SUITS]
    shuffle(deck)
    return deck
