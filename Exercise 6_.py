from tkinter import *

class MyWindow:
    def __init__(self, window):
        self.window = window
        self.lbl1 = Label(window, fg="Green", font="Georgia", text="Simple Calculator")
        self.lbl1.place(x=130, y=50)
        self.lbl2 = Label(window, fg="Green", font="Arial", text="Number 1: ")
        self.lbl2.place(x=70, y=80)
        self.t2 = Entry(window, bd=2)
        self.t2.place(x=150, y=80)
        self.lbl3 = Label(window, fg="Green", font="Arial", text="Number 2: ")
        self.lbl3.place(x=70, y=110)
        self.t3 = Entry(window, bd=2)
        self.t3.place(x=150, y=110)
        self.lbl4 = Label(window, fg="Green", font="Arial", text="Answer: ")
        self.lbl4.place(x=80, y=140)
        self.t4 = Entry(window, bd=2)
        self.t4.place(x=150, y=142)
        self.btn1 = Button(window, fg="Green", font="Arial", text="ADD", command=self.add)
        self.btn1.place(x=50, y=180)
        self.btn2 = Button(window, fg="Green", font="Arial", text="SUB", command=self.sub)
        self.btn2.place(x=110, y=180)
        self.btn3 = Button(window, fg="Green", font="Arial", text="MULTIPLY", command=self.multiply)
        self.btn3.place(x=170, y=180)
        self.btn4 = Button(window, fg="Green", font="Arial", text="DIVIDE", command=self.divide)
        self.btn4.place(x=270, y=180)

    def add(self):
        self.t4.delete(0, 'end')
        num1 = int(self.t2.get())
        num2 = int(self.t3.get())
        result = num1 + num2
        self.t4.insert('end', str(result))

    def sub(self):
        self.t4.delete(0, 'end')
        num1 = int(self.t2.get())
        num2 = int(self.t3.get())
        result = num1 - num2
        self.t4.insert('end', str(result))
    def multiply(self):
        self.t4.delete(0, 'end')
        num1 = int(self.t2.get())
        num2 = int(self.t3.get())
        result = num1 * num2
        self.t4.insert('end', str(result))
    def divide(self):
        self.t4.delete(0, 'end')
        num1 = int(self.t2.get())
        num2 = int(self.t3.get())
        result = num1 / num2
        self.t4.insert('end', str(result))

window = Tk()
mywin = MyWindow(window)
window.geometry("400x300+10+10")
window.title("Simple Calculator")
window.mainloop()
