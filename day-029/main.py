import tkinter
import os
import tkinter.messagebox
import random
import string
import pyperclip

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "logo.png")
DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.txt")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email_and_username = email_and_username_entry.get()
    password = password_entry.get()

    # messagebox

    # tkinter.messagebox.showinfo(title="Title", message="Message")
    if len(website) != 0 and len(password) != 0:
        is_ok = tkinter.messagebox.askokcancel(
            title=website,
            message=f"These are details entered: \nEmail: {email_and_username} \nPassword: {password} \nIs it ok to save?",
        )
    else:
        tkinter.messagebox.showinfo("Oops", "Please don't leave any fields empty!")
        return

    if is_ok:
        with open(DATA_FILE_PATH, mode="a") as file:
            file.write(f"{website}\t|{email_and_username}\t|{password}\n")
        entry_clear()


def entry_clear():
    website_entry.delete(0, tkinter.END)
    email_and_username_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo_image = tkinter.PhotoImage(file=IMAGE_PATH)
image_width = logo_image.width()
image_height = logo_image.height()

canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Website
website_label = tkinter.Label(text="Website:", font="Courier")
website_label.grid(column=0, row=1, sticky="W")

website_entry = tkinter.Entry(width=55)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()  # 프로그램 실행 뒤 바로 입력 가능하도록 포커싱

# Email/Username
email_and_username_label = tkinter.Label(text="Email/Username:", font="Courier")
email_and_username_label.grid(column=0, row=2, sticky="W")

email_and_username_entry = tkinter.Entry(width=55)
email_and_username_entry.grid(column=1, row=2, columnspan=2, sticky="W")

# Password

password_label = tkinter.Label(text="Password:", font="Courier")
password_label.grid(column=0, row=3, sticky="W")

password_entry = tkinter.Entry(width=30)
password_entry.grid(column=1, row=3, sticky="W")

password_button = tkinter.Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="W")

# Add

add_button = tkinter.Button(text="Add", command=add_password, width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")


window.mainloop()
