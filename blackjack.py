from random import shuffle
from card import gen_deck, Card
from enum import Enum

def get_hand_value(hand):
    return sum(map(lambda c: c.value(), hand))

class PlayerState(Enum):
    ongoing = 'ongoing'
    blackjack = 'blackjack'
    busted = 'busted'

class GameState(Enum):
    dealer_busted = 'dealer_busted'
    all_busted = 'all_busted'
    ongoing = 'ongoing'
    one_winner = 'one_winner'

class BlackjackGame:
    blackjack = 21
    dealer_bound = 17
    
    def __init__(self, num_players, callback):
        self.num_players = num_players
        self.hands = [[] for i in range(num_players + 1)]
        self.current_player = 0
        self.deck = gen_deck()
        self.states = [PlayerState.ongoing for i in range(num_players + 1)]
        self.callback = callback
        #self.draw() # TODO
        #self.draw()
        
    def _get_card(self):
        card = self.deck[-1]
        self.deck.pop()
        return card
    
    def _dispatch_callback(self, player_num):
        self.callback(player_num, self.hands[player_num], self.current_player, self.states)
        
    def _dispatch_all(self):
        for i in range(self.num_players):
            self._dispatch_callback(i)
        
    def draw(self, player_num):
        print(player_num, self.current_player)
        if player_num != self.current_player:
            return #raise Exception()
        print('a')
        card = self._get_card()
        self.hands[player_num].append(card)
        self._reeval_state(player_num)
        self._next()
        self._dispatch_all()
    
    def _next(self):
        self.current_player += 1
        while self.states[self.current_player] == PlayerState.busted or \
              self.current_player == self.num_players:
            if self.current_player == self.num_players:
                self.dealer_move()
                self.current_player = 0
            else:
                self.current_player += 1
    
    def ignore(self, player_num):
        if player_num != self.current_player:
            return #raise Exception()
        self._next()
        self._dispatch_all()
        
    def dealer_move(self):
        if get_hand_value(self.hands[-1]) < BlackjackGame.dealer_bound:
            self.hands[-1].append(self._get_card())
            self._reeval_state(self.num_players)
    
    #def get_hands(self):
        #return (self.hands, self.dealer)
    
    #def get_current_player():
        #return self.current_player
    
    def get_state(self, player_num=None):
        if player_num is None:
            return self.game_state
        return self.states[player_num]

    def _reeval_state(self, player_num):
        player_value = get_hand_value(self.hands[player_num])
        if player_value == BlackjackGame.blackjack:
            self.states[player_num] = PlayerState.blackjack
        elif player_value > BlackjackGame.blackjack:
            self.states[player_num] = PlayerState.busted
            if player_num == self.num_players:
                self.game_state = GameState.dealer_busted
