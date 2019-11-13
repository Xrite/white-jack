import tkinter as tk
from tkinter import messagebox

from blackjack import get_hand_value, BlackjackGame, GameState, PlayerState

num_players = 3
player_data = [dict() for i in range(num_players)]

def hand_str(hand):
    return "None" if len(hand) == 0 else ' '.join(map(str, hand))

def state_string(player_num, states, game_state):
    if game_state != GameState.ongoing:
        reason = None
        if game_state == GameState.dealer_busted:
            reason = "dealer busted"
        elif game_state == GameState.all_busted:
            reason = "all players busted, dealer won"
        else:
            for i, state in enumerate(states):
                if state == PlayerState.blackjack:
                    if i == player_num:
                        who = "you"
                    else:
                        who = "player #" + str(i + 1) if i < num_players else "dealer"
                    reason = who + " got blackjack"
                    break
        return "Game is over, " + reason
    busted_not_me = list(map(lambda p: str(p[0] + 1), filter(lambda p: p[1] == PlayerState.busted and p[0] != player_num, enumerate(states))))
    if len(busted_not_me) > 0:
        plural = len(busted_not_me) > 1
        state = "Player{} {} {} busted".format("s" if plural else "", ', '.join(busted_not_me), "are" if plural else "is")
        if states[player_num] == PlayerState.busted:
            state += ", btw you too"
        return state
    else:
        return "" if states[player_num] == PlayerState.ongoing else "You are busted"

def callback(player_num, current_player, player_hand, dealer_hand, states, game_state):
    data = player_data[player_num]
    data["dealer_cards"].set("Dealer cards: {}, {} points".format(hand_str(dealer_hand), get_hand_value(dealer_hand)))
    data["my_cards"].set("Your cards: {}, {} points".format(hand_str(player_hand), get_hand_value(player_hand)))
    data["state"].set(state_string(player_num, states, game_state))
    if game_state != GameState.ongoing:
        data["move"].set("")
    else:
        data["move"].set("It's {} move".format("your" if player_num == current_player else "{} player".format(current_player + 1)))
    

root = tk.Tk()

for i in range(num_players):
    window = tk.Toplevel()
    window.geometry("250x200")
    data = player_data[i]
    
    player = tk.Label(window, text="You are player #{}".format(i + 1))
    
    data["dealer_cards"] = tk.StringVar()
    dealer_cards = tk.Label(window, textvariable=data["dealer_cards"])
    
    data["my_cards"] = tk.StringVar()
    my_cards = tk.Label(window, textvariable=data["my_cards"])
    
    data["state"] = tk.StringVar()
    state = tk.Label(window, textvariable=data["state"])
    
    data["move"] = tk.StringVar()
    move = tk.Label(window, textvariable=data["move"])
    
    pass_btn = tk.Button(window, text="PASS", width=10, height=1, bg="lightgrey", fg="black")
    draw_btn = tk.Button(window, text="DRAW", width=10, height=1, bg="lightgrey", fg="black")

    pass_btn.bind("<Button>", lambda e, i=i: game.ignore(i))
    draw_btn.bind("<Button>", lambda e, i=i: game.draw(i))
    
    player.pack()
    dealer_cards.pack()
    my_cards.pack()
    state.pack()
    move.pack()
    pass_btn.pack()
    draw_btn.pack()

game = BlackjackGame(num_players, callback)
    
root.mainloop()
