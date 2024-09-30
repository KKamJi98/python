import tkinter

window = tkinter.Tk()
window.title("Tkinter Grid Challenge")
window.minsize(width=500, height=300)

label = tkinter.Label()
label.config(text="My name is Kim Tae-Ji", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)

button = tkinter.Button()
button.grid(column=1, row=1)

new_button = tkinter.Button()
button.grid(column=2, row=0)

entry = tkinter.Entry()
entry.grid(column=3, row=2)


window.mainloop()