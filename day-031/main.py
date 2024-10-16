import os
import pandas
from tkinter import PhotoImage, Tk, Canvas, Button
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
TEXT_COLOR_BLACK = "#000000"
TEXT_COLOR_WHITE = "#FFFFFF"

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "images/")
DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data/english_words.csv")
TO_LEARN_DATA_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "data/words_to_learn.csv"
)

current_card = {}
to_learn = {}

try:
    # euc-kr 인코딩으로 파일 읽기
    data = pandas.read_csv(TO_LEARN_DATA_FILE_PATH, encoding="utf-8")
except FileNotFoundError:
    original_data = pandas.read_csv(DATA_FILE_PATH, encoding="utf-8")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill=TEXT_COLOR_BLACK)
    canvas.itemconfig(card_word, text=current_card["English"], fill=TEXT_COLOR_BLACK)
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="Korean", fill=TEXT_COLOR_WHITE)
    canvas.itemconfig(card_word, text=current_card["Korean"], fill=TEXT_COLOR_WHITE)


def is_right():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv(TO_LEARN_DATA_FILE_PATH, index=False, encoding="utf-8")
    next_card()


window = Tk()  # 먼저 Tk 객체 생성
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
# 이미지를 Tk 객체 생성 이후에 초기화
card_back_image = PhotoImage(file=IMAGE_PATH + "card_back.png")
card_front_image = PhotoImage(file=IMAGE_PATH + "card_front.png")
right_button_image = PhotoImage(file=IMAGE_PATH + "right.png")
wrong_button_image = PhotoImage(file=IMAGE_PATH + "wrong.png")

canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(
    400, 150, text="", font=("Arial", 40, "italic"), fill=TEXT_COLOR_BLACK
)
card_word = canvas.create_text(
    400, 263, text="", font=("Arial", 60, "bold"), fill=TEXT_COLOR_BLACK
)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_button_image, highlightthickness=0, command=is_right)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
