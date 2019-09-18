import tkinter as tk

def pass_onclick():
    print("kek")

def draw_onclick():
    print("lol")

def get_user_cards():
    return "UC"

def get_dealer_cards():
    return "DC"

root = tk.Tk()

root.geometry("800x600")

user_cards = tk.Label(root, text=get_user_cards())
dealer_cards = tk.Label(root, text=get_dealer_cards())

pass_btn = tk.Button(root, text="PASS", width=10, height=5, bg="lightgrey", fg="black")
draw_btn = tk.Button(root, text="DRAW", width=10, height=5, bg="lightgrey", fg="black")

user_cards.pack()
dealer_cards.pack()
pass_btn.pack()
draw_btn.pack()
main_frame.pack()

root.mainloop()