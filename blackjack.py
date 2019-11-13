from random import shuffle
from card import gen_deck, Card

class BlackjackGame:

    def __init__(self):
        self.new_game()
        
    def new_game(self):
        self.player = []
        self.dealer = []
        self.deck = gen_deck()
        self.state = 'ongoing'
        self.draw()
        self.draw()
        
    def get_card(self):
        card = self.deck[-1]
        self.deck.pop()
        return card
        
    def draw(self):
        self.player.append(self.get_card())
        self.reeval_state()
        if self.state != 'ongoing':
            return
        self.ignore()
    
    def ignore(self):
        if get_hand_value(self.dealer) < 17:
            self.dealer.append(self.get_card())
            self.reeval_state()
        else:
            player_value = get_hand_value(self.player)
            dealer_value = get_hand_value(self.dealer)
            if player_value < dealer_value:
                self.state = 'dealerwin'
            elif player_value == dealer_value:
                self.state = 'draw'
            else:
                self.state = 'playerwin'
    
    def get_dealer_hand(self):
        return self.dealer
    
    def get_player_hand(self):
        return self.player
    
    def get_state(self):
        return self.state

    def reeval_state(self):
        player_value = get_hand_value(self.player)
        dealer_value = get_hand_value(self.dealer)
        if player_value == 21:
            self.state = 'playerwin'
        elif player_value > 21:
            self.state = 'dealerwin'
        elif dealer_value > 21:
            self.state = 'playerwin'
            
def get_hand_value(hand):
    return sum(map(Card.value, hand))

def get_card_value(card):
    if card[0].isdigit():
        if card[0] == '1':
            return int(card[:2])
        else:
            return int(card[0])
    else:
        if card[0] == 'A':
            return 11
        else:
            return 10
