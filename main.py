import tkinter
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = [*letter_list, *symbol_list, *number_list]

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    # Auto copies the password onto clipboard-
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        isok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                             f"\nPassword: {password} \nis this info correct?")
        if isok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
            web_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)
canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
web_label = tkinter.Label(text="Website:")
web_label.grid(column=0, row=1)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_label = tkinter.Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entries
web_entry = tkinter.Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky="w")
web_entry.focus()
email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "eanthonyj001@gmail.com")
pass_entry = tkinter.Entry(width=30)
pass_entry.grid(column=1, row=3, sticky="w")

# Buttons
gen_pass = tkinter.Button(text="Generate Password", command=pass_gen)
gen_pass.grid(column=2, row=3, sticky="w")
add = tkinter.Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
