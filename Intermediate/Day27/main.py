from tkinter import *

from click import command


def mile_to_km():
	miles = float(miles_input.get())
	km = miles * 1.609
	kilometer_result.config(text= f"{km}")

window = Tk()
window.title("Mile to Kilometer convertor")
window.minsize(width=500, height=500)
window.config(padx=20 , pady=20)
miles_input = Entry(width=8)
miles_input.grid(column=1, row= 0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
is_equal_to = Label(text="equal to")
is_equal_to.grid(column=0, row=1)
kilometer_result = Label(text= "0")
kilometer_result.grid(column=1, row= 1)
kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row=1)
calculate_button = Button(text="Button", command=mile_to_km)
calculate_button.grid(column=1, row=2)
window.mainloop()
