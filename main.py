from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# Data Read
data_dictionary = {}
current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dictionary = data.to_dict(orient="records")
else:
    data_dictionary = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dictionary)
    current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=change_card)


def known_card():
    data_dictionary.remove(current_card)
    new_data = pandas.DataFrame(data_dictionary)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def change_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# UI
window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=change_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Courier", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Courier", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
next_button = Button(image=cross_image, highlightthickness=0, command=next_card)
next_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
check_button = Button(image=right_image, highlightthickness=0, command=known_card)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()
