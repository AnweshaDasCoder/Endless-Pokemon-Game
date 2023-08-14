from tkinter import*
from PIL import ImageTk, Image
import random
root=Tk()

root.title("Endless Pokemon Game")
root.geometry("600x400")

root.configure(background="dark orange")

Pokemon1 = Label(root, text = "Player 1", bg = "CadetBlue1")
Pokemon1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

Pokemon2 = Label(root, text = "Player 2", bg = "CadetBlue1")
Pokemon2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

Pokemon1_score = Label(root, bg = "CadetBlue1")
Pokemon1_score .place(relx = 0.1, rely = 0.4, anchor = CENTER)

Pokemon1_score  = Label(root, bg = "CadetBlue1")
Pokemon1_score.place(relx = 0.9, rely = 0.4, anchor = CENTER)

pokemon_card_label = Label(root)
pokemon_card_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()