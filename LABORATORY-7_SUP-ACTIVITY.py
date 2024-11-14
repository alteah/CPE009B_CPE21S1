import tkinter as tk
import math

# Functions for calculation
def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 + num2)
        add_to_history(f"{num1} + {num2} = {num1 + num2}")
    except ValueError:
        result.set("Invalid input!")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 - num2)
        add_to_history(f"{num1} - {num2} = {num1 - num2}")
    except ValueError:
        result.set("Invalid input!")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 * num2)
        add_to_history(f"{num1} * {num2} = {num1 * num2}")
    except ValueError:
        result.set("Invalid input!")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            result.set("Error! Division by zero.")
        else:
            result.set(num1 / num2)
            add_to_history(f"{num1} / {num2} = {num1 / num2}")
    except ValueError:
        result.set("Invalid input!")

def square_root():
    try:
        num = float(entry1.get())
        if num < 0:
            result.set("Error! Negative number for square root.")
        else:
            result.set(math.sqrt(num))
            add_to_history(f"√{num} = {math.sqrt(num)}")
    except ValueError:
        result.set("Invalid input!")

def power():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(math.pow(num1, num2))
        add_to_history(f"{num1} ^ {num2} = {math.pow(num1, num2)}")
    except ValueError:
        result.set("Invalid input!")

def sine():
    try:
        num = float(entry1.get())
        result.set(math.sin(math.radians(num)))
        add_to_history(f"sin({num}) = {math.sin(math.radians(num))}")
    except ValueError:
        result.set("Invalid input!")

def cosine():
    try:
        num = float(entry1.get())
        result.set(math.cos(math.radians(num)))
        add_to_history(f"cos({num}) = {math.cos(math.radians(num))}")
    except ValueError:
        result.set("Invalid input!")

def tangent():
    try:
        num = float(entry1.get())
        result.set(math.tan(math.radians(num)))
        add_to_history(f"tan({num}) = {math.tan(math.radians(num))}")
    except ValueError:
        result.set("Invalid input!")

# Add operation to history
def add_to_history(operation):
    history_list.insert(tk.END, operation)
    history_list.yview(tk.END)

# Function to clear the input fields and result
def clear():
    entry1.delete(0, tk.END)  # Clear the first entry field
    entry2.delete(0, tk.END)  # Clear the second entry field
    result.set("")            # Clear the result
    history_list.delete(0, tk.END)  # Clear the history

# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")

# Styling
root.config(bg='white')  # Background color
font = ("Arial", 12)

# Create StringVar to hold the result
result = tk.StringVar()

# Create the layout
tk.Label(root, text="Enter first number:", font=font, bg='#f4f4f4').grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root, font=font, bd=3, relief="solid")
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Enter second number:", font=font, bg='#f4f4f4').grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root, font=font, bd=3, relief="solid")
entry2.grid(row=1, column=1, padx=5, pady=5)

# Buttons for operations
button_style = {"font": font, "bg": "black", "fg": "white", "padx": 10, "pady": 5}

tk.Button(root, text="Add", command=add, **button_style).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="Subtract", command=subtract, **button_style).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Multiply", command=multiply, **button_style).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="Divide", command=divide, **button_style).grid(row=3, column=1, padx=5, pady=5)

tk.Button(root, text="Square Root", command=square_root, **button_style).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text="Power", command=power, **button_style).grid(row=4, column=1, padx=5, pady=5)

tk.Button(root, text="Sine", command=sine, **button_style).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="Cosine", command=cosine, **button_style).grid(row=5, column=1, padx=5, pady=5)
tk.Button(root, text="Tangent", command=tangent, **button_style).grid(row=6, column=0, padx=5, pady=5)

# Clear Button
tk.Button(root, text="Clear", command=clear, **button_style).grid(row=6, column=1, padx=5, pady=5)

# Label to show result
tk.Label(root, text="Result:", font=font, bg='#f4f4f4').grid(row=7, column=0, padx=5, pady=5)
result_label = tk.Label(root, textvariable=result, font=font, bg='#f4f4f4', bd=3, relief="solid", width=20)
result_label.grid(row=7, column=1, padx=5, pady=5)

# History Listbox
tk.Label(root, text="History:", font=font, bg='#f4f4f4').grid(row=8, column=0, padx=5, pady=5)
history_list = tk.Listbox(root, font=font, height=5, width=40, bd=3, relief="solid")
history_list.grid(row=8, column=1, padx=5, pady=5)

# Start the main loop
root.mainloop()
