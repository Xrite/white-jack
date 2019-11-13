import tkinter as tk
from tkinter import messagebox

from blackjack import BlackjackGame

def refresh(game, user_cards_var, dealer_cards_var):
    user_cards_var.set("Your cards: {}".format(get_user_cards(game)))
    dealer_cards_var.set("Dealer cards: {}".format(get_dealer_cards(game)))

def check_state(game):
    global root
    if game.get_state() == GameState.ongoing:
        return
    else:
        messagebox.showinfo(game.get_state().name, "Lol")
        root.destroy()

def pass_onclick(game, user_cards_var, dealer_cards_var):
    game.ignore()
    refresh(game, user_cards_var, dealer_cards_var)
    check_state(game)

def draw_onclick(game, user_cards_var, dealer_cards_var):
    game.draw()
    refresh(game, user_cards_var, dealer_cards_var)
    check_state(game)

def get_user_cards(game):
    cards = game.get_player_hand()
    return ' '.join(map(str, cards))

def get_dealer_cards(game):
    cards = game.get_dealer_hand()
    return ' '.join(map(str, cards))

def init_root(game, height, weight):
    root = tk.Tk()
    root.geometry("{}x{}".format(w, h))

    pass_btn = tk.Button(root, text="PASS", width=10, height=5, bg="lightgrey", fg="black")
    draw_btn = tk.Button(root, text="DRAW", width=10, height=5, bg="lightgrey", fg="black")

    pass_btn.bind("<Button>", lambda event: pass_onclick(game, user_cards_var, dealer_cards_var))
    draw_btn.bind("<Button>", lambda event: draw_onclick(game, user_cards_var, dealer_cards_var))

    user_cards_var = tk.StringVar()
    dealer_cards_var = tk.StringVar()
    refresh(game, user_cards_var, dealer_cards_var)

    user_cards = tk.Label(root, textvariable=user_cards_var)
    dealer_cards = tk.Label(root, textvariable=dealer_cards_var)

    user_cards.pack()
    dealer_cards.pack()

    pass_btn.pack()
    draw_btn.pack()


game = BlackjackGame()
root = init_root(game, 800, 600)
root.mainloop()