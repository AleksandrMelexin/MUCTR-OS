from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random


def get_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def change(n):
    root["bg"] = get_rgb((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    print(n)


root = Tk()  # создаем корневой объект - окно
root.title("Задание 3")  # устанавливаем заголовок окна
root.geometry("600x600")  # устанавливаем размеры окна
root.resizable(False, False)

root.bind("<Motion>", change)

root.mainloop()
