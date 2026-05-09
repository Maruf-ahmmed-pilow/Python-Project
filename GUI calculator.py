import tkinter as tk

# Function to calculate result
def click(event):
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, text)

# Main window
root = tk.Tk()
root.title("GUI Calculator")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for button in row:
        btn = tk.Button(frame, text=button, font="Arial 18")
        btn.pack(side="left", expand=True, fill="both")

        btn.bind("<Button-1>", click)

# Clear button
clear_btn = tk.Button(root, text="C", font="Arial 18", bg="red", fg="white")
clear_btn.pack(fill="both", padx=10, pady=5)

clear_btn.bind("<Button-1>", click)

# Run app
root.mainloop()