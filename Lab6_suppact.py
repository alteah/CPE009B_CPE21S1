import tkinter as tk
from tkinter import Menu, messagebox, filedialog
import math

# Initialize main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

# Input field
input_text = tk.StringVar()
entry = tk.Entry(root, textvariable=input_text, font=('Arial', 24), justify='right', bd=10)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Functions for Calculator
def clear():
    input_text.set("")

def add_to_expression(value):
    input_text.set(input_text.get() + str(value))

def calculate():
    try:
        result = eval(input_text.get())
        input_text.set(result)
        save_calculation(input_text.get())
    except Exception as e:
        input_text.set("Error")

def trig_function(func):
    try:
        expression = input_text.get()
        result = getattr(math, func)(math.radians(float(expression)))
        input_text.set(result)
        save_calculation(f"{func}({expression}) = {result}")
    except Exception as e:
        input_text.set("Error")

def exponentiate():
    try:
        expression = input_text.get()
        base, exponent = map(float, expression.split('^'))
        result = math.pow(base, exponent)
        input_text.set(result)
        save_calculation(f"{base}^{exponent} = {result}")
    except Exception as e:
        input_text.set("Error")

def save_calculation(calculation):
    with open("calculations.txt", "a") as file:
        file.write(calculation + "\n")

def view_calculations():
    with open("calculations.txt", "r") as file:
        content = file.read()
    messagebox.showinfo("Saved Calculations", content)

def exit_app():
    root.quit()

# Menu Bar
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Clear", command=clear)
file_menu.add_command(label="View Calculations", command=view_calculations)
file_menu.add_separator()
file_menu.add_command(label="Exit (Ctrl+Q)", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)
root.bind('<Control-q>', lambda e: exit_app())

# Calculator Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('^', 5, 1), ('sin', 5, 2), ('cos', 5, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=10, height=3, command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=10, height=3, command=clear)
    elif text == 'sin':
        btn = tk.Button(root, text=text, width=10, height=3, command=lambda: trig_function('sin'))
    elif text == 'cos':
        btn = tk.Button(root, text=text, width=10, height=3, command=lambda: trig_function('cos'))
    elif text == '^':
        btn = tk.Button(root, text=text, width=10, height=3, command=exponentiate)
    else:
        btn = tk.Button(root, text=text, width=10, height=3, command=lambda t=text: add_to_expression(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
