import tkinter

# 컴포넌트를 배치하는 방법에는 pack, place, grid가 있다
window = tkinter.Tk()  # 객체 초기화/ 윈도우 생성
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text2")
# my_label["text"] = "New Text"
my_label.grid(column=0, row=0)
# my_label.place(x=100, y=200)
# my_label.pack(side="left")
# my_label.pack()


def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=input.get())


# Button

button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack(side="left")
button.grid(column=1, row=1)

# Entry Component

input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=2, row=2)
# input.pack()


window.mainloop()  # 윈도우가 스크린에 계속 유지되도록 하며 사용자가 윈도우와 상호 작용하는 것을 Listening함
