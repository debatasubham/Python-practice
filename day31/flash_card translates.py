from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
CURRENT_DIR = os.path.dirname(__file__)

current_card = {}
to_learn = []
flip_timer = None

try:
    data_path = os.path.join(CURRENT_DIR, "words_to_learn.csv")
    if os.path.exists(data_path):
        data = pd.read_csv(data_path)
    else:
        data = pd.read_csv(os.path.join(CURRENT_DIR, "french_words.csv"))
    to_learn = data.to_dict(orient="records")
except Exception:
    original_data = pd.read_csv(os.path.join(CURRENT_DIR, "french_words.csv"))
    to_learn = original_data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    if flip_timer is not None:
        try:
            window.after_cancel(flip_timer)
        except TclError:
            pass
        flip_timer = None
    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text="Completed!", fill="black")
        canvas.itemconfig(card_word, text="No more words to learn", fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        return

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    if current_card:
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")
        canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    if current_card in to_learn:
        to_learn.remove(current_card)
        new_data = pd.DataFrame(to_learn)
        new_data.to_csv(os.path.join(CURRENT_DIR, "words_to_learn.csv"), index=False)
    next_card()


window = Tk()
window.title("Flash Card Translates")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=os.path.join(CURRENT_DIR, "card_front.png"))
card_back_img = PhotoImage(file=os.path.join(CURRENT_DIR, "card_back.png"))
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file=os.path.join(CURRENT_DIR, "wrong.png"))
unknown_button = Button(image=cross_image, highlightthickness=0, bd=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=os.path.join(CURRENT_DIR, "right.png"))
known_button = Button(image=check_image, highlightthickness=0, bd=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()