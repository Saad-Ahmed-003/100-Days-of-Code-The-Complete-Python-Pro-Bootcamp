from p_data import letters, numbers, symbols
from tkinter import messagebox
from tkinter import *
import pyperclip
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
Password_list = []


def password_generator():
    password = ""
    for i in range(4):
        data = random.choice(letters)
        Password_list.append(data)
    for i in range(2):
        data = random.choice(symbols)
        Password_list.append(data)
    for i in range(2):
        data = random.choice(numbers)
        Password_list.append(data)
    random.shuffle(Password_list)
    for i in Password_list:
        password += i
    random.shuffle(Password_list)
    for i in Password_list:
        password += i
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                       f"\nPassword: {password} \nIs it ok to save?")
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#222222")

canvas = Canvas(height=208, width=200, bg="#222222", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", fg="#E6DDC4", bg="#222222")
website_label.grid(row=1, column=0)
email_label = Label(text="E-mail/Username:", fg="#E6DDC4", bg="#222222")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", fg="#E6DDC4", bg="#222222")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "learn.saad.dev03@gmail.com")
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=password_generator, bg="#B2B2B2",
                                  highlightthickness=0)
generate_password_button.grid(row=3, column=2, columnspan=1)
add_button = Button(text="Add", width=34, command=save, bg="#B2B2B2", highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
