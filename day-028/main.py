from tkinter import *
import os

# ---------------------------- CONSTANTS ------------------------------- #
IMAGE_PATH = os.path.join(os.path.dirname(__file__), "tomato.png")
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

# 배경

tomato_image = PhotoImage(file=IMAGE_PATH)
image_width = tomato_image.width()
image_height = tomato_image.height()

canvas = Canvas(width=image_width, height=image_height, bg=YELLOW, highlightthickness=0)
canvas.create_image(image_width/2, image_height/2, image=tomato_image)
canvas.create_text(image_width/2, image_height/2+18, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text="\u2705", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
check_marks.grid(column=1, row=3)



window.mainloop()