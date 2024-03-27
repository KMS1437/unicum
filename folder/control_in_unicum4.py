from tkinter import *
import random

def first():
    def Hello(event):
        label.config(text="Hello Word!")
    root = Tk()
    root.title("1 задание")
    label = Label(root, text="")
    label.pack()
    root.bind("<Return>", Hello)
    root.mainloop()

def second():
    def calculate():
        a = float(entry_1.get())
        b = float(entry_2.get())

        if operation.get() == "+":
            res = a + b
        elif operation.get() == "-":
            res = a - b

        label.config(text=res)

    root = Tk()
    root.title("2 задание (Калькулятор)")
    entry_1 = Entry(root)
    entry_1.pack()
    entry_2 = Entry(root)
    entry_2.pack()
    operation = StringVar(root)
    plus = Button(root, text="+", command=lambda: operation.set("+"))
    plus.pack()
    minus = Button(root, text="-", command=lambda: operation.set("-"))
    minus.pack()
    equals = Button(root, text="=", command=calculate)
    equals.pack()
    label = Label(root, text="")
    label.pack()
    root.mainloop()

def third():
    def create_circle(event):
        x = random.randint(10, 390)
        y = random.randint(10, 390)
        radius = 10
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius)

    root = Tk()
    root.title("3 задание (круги)")
    canvas = Canvas(root, width=400, height=400)
    canvas.pack()
    canvas.bind("<Button-1>", create_circle)
    root.mainloop()

root = Tk()
root.title("Выберите задачу уровня B")

def choice(choice):
    if choice == 1:
        first()
    elif choice == 2:
        second()
    elif choice == 3:
        third()
      
button_1 = Button(root, text="1", command=lambda: choice(1))
button_1.pack()
button_2 = Button(root, text="2", command=lambda: choice(2))
button_2.pack()
button_3 = Button(root, text="3", command=lambda: choice(3))
button_3.pack()
root.mainloop()
