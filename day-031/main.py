import os
from tkinter import PhotoImage, Tk, Canvas, Button

BACKGROUND_COLOR = "#B1DDC6"

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "images/")

window = Tk()  # 먼저 Tk 객체 생성
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# 이미지를 Tk 객체 생성 이후에 초기화
card_back_image = PhotoImage(file=IMAGE_PATH+"card_back.png")
card_front_image = PhotoImage(file=IMAGE_PATH+"card_front.png")
right_button_image = PhotoImage(file=IMAGE_PATH+"right.png")
wrong_button_image = PhotoImage(file=IMAGE_PATH+"wrong.png")

canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_button_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_button_image, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()