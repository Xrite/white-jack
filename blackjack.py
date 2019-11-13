from random import shuffle
from card import gen_deck

class BlackjackGame:
    blackjack = 21
    dealer_bound = 17
    
    def __init__(self):
        self.new_game()
        
    def new_game(self, num_players):
        self.num_players = num_players
        self.hands = [[] for i in range(num_players)]
        self.dealer = []
        self.current_player
        self.deck = gen_deck()
        self.states = 'ongoing'
        self.draw() # TODO
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
        if get_hand_value(self.dealer) < dealer_bound:
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
    
    def get_hands(self):
        return (self.hands, self.dealer)
    
    def get_current_player():
        return self.current_player
    
    def get_state(self, player_num):
        return self.states[player_num]

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
    return sum(map(get_card_value, hand))
