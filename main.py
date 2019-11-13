import tkinter as tk
from tkinter import messagebox

from blackjack import BlackjackGame


def callback(player_num, player_hand, current, states):
    user_cards_vars[player_num].set("Your cards: {0}".format(' '.join(map(str, cards))))

root = tk.Tk()

num_players = 3
game = BlackjackGame(num_players, callback)
user_cards_vars = [None for i in range(num_players)]


for i in range(num_players):
    window = tk.Toplevel()
    window.geometry("300x200")
    
    player = tk.Label(window, text="You are player #{}".format(i))
    player.pack()

    pass_btn = tk.Button(window, text="PASS", width=10, height=3, bg="lightgrey", fg="black")
    draw_btn = tk.Button(window, text="DRAW", width=10, height=3, bg="lightgrey", fg="black")

    pass_btn.bind("<Button>", lambda event: game.ignore(i))
    draw_btn.bind("<Button>", lambda event: game.draw(i))

    user_cards_vars[i] = tk.StringVar()
    user_cards_vars[i].set('Empty hand')

    user_cards = tk.Label(window, textvariable=user_cards_vars[i])

    user_cards.pack()

    pass_btn.pack()
    draw_btn.pack()

root.mainloop()
