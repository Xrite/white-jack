import tkinter as tk
from tkinter import messagebox

from blackjack import BlackjackGame

def refresh(game, user_cards_var, dealer_cards_var):
    user_cards_var.set("Your cards: {0}".format(get_user_cards(game)))
    dealer_cards_var.set("Dealer cards: {0}".format(get_dealer_cards(game)))

def check_state(game):
    global root
    if game.get_state() == "ongoing":
        return
    elif game.get_state() == "dealerwin":
        messagebox.showinfo("Dealer win", "Lol")
        root.destroy()
    elif game.get_state() == "playerwin":
        messagebox.showinfo("Player win", "Lol")
        root.destroy()
    elif game.get_state() == "draw":
        messagebox.showinfo("Draw", "Lol")
        root.destroy()
    else:
        raise ValueError("Unexpected state")

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
    return ' '.join(cards)

def get_dealer_cards(game):
    cards = game.get_dealer_hand()
    return ' '.join(cards)

root = tk.Tk()

root.geometry("800x600")

pass_btn = tk.Button(root, text="PASS", width=10, height=5, bg="lightgrey", fg="black")
draw_btn = tk.Button(root, text="DRAW", width=10, height=5, bg="lightgrey", fg="black")

pass_btn.bind("<Button>", lambda event: pass_onclick(game, user_cards_var, dealer_cards_var))
draw_btn.bind("<Button>", lambda event: draw_onclick(game, user_cards_var, dealer_cards_var))

game = BlackjackGame()

user_cards_var = tk.StringVar()
user_cards_var.set("Your cards: {0}".format(get_user_cards(game)))

dealer_cards_var = tk.StringVar()
dealer_cards_var.set("Dealer cards: {0}".format(get_dealer_cards(game)))

user_cards = tk.Label(root, textvariable=user_cards_var)
dealer_cards = tk.Label(root, textvariable=dealer_cards_var)

user_cards.pack()
dealer_cards.pack()

pass_btn.pack()
draw_btn.pack()

root.mainloop()