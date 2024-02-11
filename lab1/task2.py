from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def right(x):
    label2["text"] = "Пришёл"
    label1["text"] = "Ушёл"


def left(x):
    label2["text"] = "Ушёл"
    label1["text"] = "Пришёл"


def unkhown(x):
    label2["text"] = "Ушёл"
    label1["text"] = "Ушёл"


root = Tk()  # создаем корневой объект - окно
root.title("Задание 2")  # устанавливаем заголовок окна
root.geometry("600x140")  # устанавливаем размеры окна
root.resizable(False, False)
empty = ttk.Label(text="", padding=150, foreground="#000000", background="#FFFFFF")
empty.place(x=175, y=0)
empty.bind("<Motion>", unkhown)
label1 = ttk.Label(text="Ушёл", padding=70, foreground="#000000", background="#FFCC00")
label1.place(x=0, y=0)
label1.bind("<Motion>", left)
label2 = ttk.Label(text="Ушёл", padding=70, foreground="#000000", background="#FFCC00")
label2.place(x=430, y=0)
label2.bind("<Motion>", right)

root.mainloop()
