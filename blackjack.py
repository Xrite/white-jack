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
        self.game_state = GameState.ongoing
        self.callback = callback
        self.count_busted = 0
        for i in range(num_players):
            self.draw(i)
        self._dispatch_all()
        
    def _get_card(self):
        card = self.deck[-1]
        self.deck.pop()
        return card
    
    def _dispatch_callback(self, player_num):
        self.callback(player_num, self.current_player, self.hands[player_num], self.hands[-1], self.states, self.game_state)
        
    def _dispatch_all(self):
        for i in range(self.num_players):
            self._dispatch_callback(i)
        
    def draw(self, player_num):
        if player_num != self.current_player:
            return
        card = self._get_card()
        self.hands[player_num].append(card)
        self._reeval_state(player_num)
        if self.game_state == GameState.ongoing:
            self._next()
        self._dispatch_all()
    
    def _next(self):
        self.current_player += 1
        while (self.states[self.current_player] == PlayerState.busted or \
               self.current_player == self.num_players) and \
               self.game_state == GameState.ongoing:
            if self.current_player == self.num_players:
                self.dealer_move()
                self.current_player = 0
            else:
                self.current_player += 1
    
    def ignore(self, player_num):
        if player_num != self.current_player:
            return
        self._next()
        self._dispatch_all()
        
    def dealer_move(self):
        if get_hand_value(self.hands[-1]) < BlackjackGame.dealer_bound:
            self.hands[-1].append(self._get_card())
            self._reeval_state(self.num_players)

    def _reeval_state(self, player_num):
        player_value = get_hand_value(self.hands[player_num])
        if player_value == BlackjackGame.blackjack:
            self.states[player_num] = PlayerState.blackjack
            self.game_state = GameState.one_winner
        elif player_value > BlackjackGame.blackjack:
            self.states[player_num] = PlayerState.busted
            self.count_busted += 1
            if player_num == self.num_players:
                self.game_state = GameState.dealer_busted
            elif self.count_busted == self.num_players:
                self.game_state = GameState.all_busted
