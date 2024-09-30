import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=10)

# Label

mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

result_label = tkinter.Label(text=0)
result_label.grid(column=1, row=1)

# Button


def convert_mile_to_km():
    miles = float(mile_entry.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


calculate_button = tkinter.Button(text="Calculate", command=convert_mile_to_km)
calculate_button.grid(column=1, row=2)

# Entry

mile_entry = tkinter.Entry(width=7)
mile_entry.grid(column=1, row=0)

window.mainloop()
