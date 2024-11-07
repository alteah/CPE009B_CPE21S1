from tkinter import *

class MyWindow:
    def __init__(self, window):
        self.window = window
        self.btn1 = Button(window, fg="Black", font="Georgia", text="Click to Change Color" , command=self.change_color, bg = "White")
        self.btn1.place(x=115, y=110)

        window.config(bg="White")

    def change_color(self):
            self.Button = Button(font = "Georgia" , text =" Click to change color  ", bg = "Yellow")
            self.Button.place(x=115, y=110)

window = Tk()
mywin = MyWindow(window)
window.geometry("400x300+10+10")
window.title("Special Midterm Exam in OOP")
window.mainloop()






