import tkinter
import os
import tkinter.messagebox
import random
import string
import pyperclip
import json

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "logo.png")
DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.json")


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
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    # messagebox

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        try:
            with open(DATA_FILE_PATH, "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
        except FileNotFoundError:
            with open(DATA_FILE_PATH, "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open(DATA_FILE_PATH, "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            # email_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    try:
        with open(DATA_FILE_PATH, "r") as data_file:
            data = json.load(data_file)
            print(data)
            website = website_entry.get()
            email = data[website]["email"]
            password = data[website]["password"]
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="Error", message="No Data File Found.")
    except KeyError:
        tkinter.messagebox.showinfo(
            title="Error", message=f"No Details for the {website} exists."
        )
    else:
        tkinter.messagebox.showinfo(
            title=website_entry.get(), message=f"Email: {email}\nPassword: {password}"
        )


def entry_clear():
    website_entry.delete(0, tkinter.END)
    email_entry.delete(0, tkinter.END)
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

website_entry = tkinter.Entry(width=30)
website_entry.grid(column=1, row=1, sticky="W")
website_entry.focus()  # 프로그램 실행 뒤 바로 입력 가능하도록 포커싱

search_button = tkinter.Button(width=20, text="Search", command=search_password)
search_button.grid(column=2, row=1, sticky="W")

# Email/Username
email_and_username_label = tkinter.Label(text="Email/Username:", font="Courier")
email_and_username_label.grid(column=0, row=2, sticky="W")

email_entry = tkinter.Entry(width=57)
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")

# Password

password_label = tkinter.Label(text="Password:", font="Courier")
password_label.grid(column=0, row=3, sticky="W")

password_entry = tkinter.Entry(width=30)
password_entry.grid(column=1, row=3, sticky="W")

password_button = tkinter.Button(
    width=20, text="Generate Password", command=generate_password
)
password_button.grid(column=2, row=3, sticky="W")

# Add

add_button = tkinter.Button(text="Add", command=add_password, width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")


window.mainloop()
