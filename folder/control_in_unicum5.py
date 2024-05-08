import math
import tkinter as tk

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def print(self):
        print(f"Круг на координатах {self.x}, {self.y} с радиусом {self.r} имеет площадь {self.area()}")

    def paint(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, outline="red")

class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def print(self):
        print(f"Прямоугольник на координатах {self.x}, {self.y} с шириной {self.width} и высотой {self.height} имеет площадь {self.area()}")

    def paint(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, outline="red")

def create_window(figure):
    window = tk.Tk()
    canvas = tk.Canvas(window, width=400, height=250)
    canvas.pack()
    window.geometry("400x250")
    window.title("Контрольная")
    figure.paint(canvas)
    window.mainloop()

def figures():
    circle1 = Circle(10, 20, 50)
    circle2 = Circle(80, 90, 10)
    rect1 = Rect(10, 20, 20, 30)

    create_window(circle1)
    create_window(circle2)
    create_window(rect1)

figures()
