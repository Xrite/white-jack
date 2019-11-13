from random import shuffle
from card import gen_deck, Card

class BlackjackGame:
    blackjack = 21
    dealer_bound = 17
    
    def __init__(self):
        self.new_game()
        
    def new_game(self, num_players):
        self.num_players = num_players
        self.hands = [[] for i in range(num_players + 1)]
        self.current_player = 0
        self.deck = gen_deck()
        self.states = ['ongoing' for i in range(num_players + 1)]
        self.draw() # TODO
        self.draw()
        
    def _get_card(self):
        card = self.deck[-1]
        self.deck.pop()
        return card
        
    def draw(self, player_num):
        if player_num != self.current_player:
            raise Exception()
        card = self._get_card()
        self.players[player_num].append(card)
        self.reeval_state(player_num)
        self.ignore(player_num)
        return card
    
    def ignore(self, player_num):
        self.current_player += 1
        if self.current_player == self.num_players:
            self.dealer_move()
            self.current_player = 0
        # TODO
                
    def dealer_move(self):
        if get_hand_value(self.dealer) < dealer_bound:
            self.dealer.append(self._get_card())
            self.reeval_state(self.num_players)
    
    #def get_hands(self):
        #return (self.hands, self.dealer)
    
    def get_current_player():
        return self.current_player
    
    def get_state(self, player_num):
        return self.states[player_num]

    def _reeval_state(self, player_num):
        player_values = get_hand_value(self.player)
        if player_value == blackjack:
            self.states[player_num] = 'blackjack'
        elif player_value > blackjack:
            self.states[player_num] = 'busted'
            
def get_hand_value(hand):
    return sum(map(get_card_value, hand))
