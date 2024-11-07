from tkinter import *

class MyWindow:
    def __init__(self, window):
        self.window = window
        self.lbl1 = Label(window, fg="Red", font="Arial", text="Enter your full name: ")
        self.lbl1.place(x=80, y=80)
        self.t1 = Entry(window, bd=2)
        self.t1.place(x=300, y=80)

        self.btn1 = Button(window, fg="Red", font="Arial", text="Click to display your full name: ",command = self.display)
        self.btn1.place(x=80, y=120)

        self.t2 = Entry(window, bd=2)
        self.t2.place(x=310, y=125)


        window.config(bg="White")

    def display(self):
            self.t2.delete(0, 'end')
            name = str(self.t1.get())
            self.t2.insert(END, str(name))






window = Tk()
mywin = MyWindow(window)
window.geometry("600x300+10+10")
window.title("Simple Calculator")
window.mainloop()