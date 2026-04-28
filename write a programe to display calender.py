# import calendar
# year = int(input('Enter year: '))
# month = int(input('Enter month: '))
# cal = calendar.month(year, month)
# print(cal)

import calendar
import tkinter as tk

def show_calendar():
    year = int(entry.get())
    cal_text = calendar.calendar(year)
    output_label.config(text=cal_text)

# window create
root = tk.Tk()
root.title("Calendar App")

# input field
entry = tk.Entry(root)
entry.pack()

# button
btn = tk.Button(root, text="Show Calendar", command=show_calendar)
btn.pack()

# output
output_label = tk.Label(root, font=("Courier", 10), justify="left")
output_label.pack()

root.mainloop()

