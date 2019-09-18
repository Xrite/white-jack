from random import shuffle

class BlackjackGame:
    suits = ['♦', '♣', '♥', '♠']
    faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self):
        self.new_game()
        
    def new_game(self):
        self.player = []
        self.dealer = []
        self.deck = gen_deck()
        self.state = 'ongoing'
        
        
    def draw(self):
        
    
    def fuck(self):
        pass
    
    def get_dealer_hand(self):
        return self.dealer
    
    def get_player_hand(self):
        return self.player
    
    def get_state(self):
        return self.state
    
    def gen_deck():
        deck = [face + suit for face in BlackjackGame.faces for suit in BlackjackGame.suits]
        shuffle(deck)
        return deck
    
    def get_card_value(card):
        if card.isdigit():
            if card[0] == '1':
                return int(card[:2])
            else:
                return int(card[0])
        else:
            if card[0] == 'A':
                return 11
            else:
                return 10
            
    def get_hand_value(hand):
        return sum(map(get_card_value, hand))
