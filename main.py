from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=30, pady=10)


def convert_mile_km():
    user_input = mile_input.get()
    km_result = float(user_input) * 1.609
    kilometer_result.config(text=round(km_result, 2))


mile_input = Entry(width=10)
mile_input.grid(column=2, row=0)

label_mile = Label(text="Miles")
label_mile.grid(column=3, row=0)

is_eq_label = Label(text="is equal to")
is_eq_label.grid(column=1, row=1)

kilometer_result = Label(text=0)
kilometer_result.grid(column=2, row=1)

label_km = Label(text="km")
label_km.grid(column=3, row=1)

cal_button = Button(text="Calculate", command=convert_mile_km)
cal_button.grid(column=2, row=2)

window.mainloop()
