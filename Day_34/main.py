from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
language = "Title"
word = "Word"
language_font = ("Ariel", 40, "italic")
word_font = ("Ariel", 60, "bold")

# -------------------------------------- UI SETUP -------------------------------------- #

# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# image aligning
canvas = Canvas(height=530, width=820)
canvas.create_image(420, 270, image=card_front_img)
canvas.grid(row=0, column=1, columnspan=6, rowspan=4)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# button aligning
right_btn = Button(image=right_img, highlightthickness=0)
right_btn.grid(row=4, column=5)
wrong_btn = Button(image=wrong_img, highlightthickness=0)
wrong_btn.grid(row=4, column=2)

# label aligning
language_title = Label(text=f"{language}", font=language_font)
language_title.grid(row=1, column=3, columnspan=2)
word_title = Label(text=f"{word}", font=word_font)
word_title.grid(row=2, column=3, columnspan=2)

window.mainloop()
