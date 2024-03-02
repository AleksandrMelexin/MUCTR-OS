from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import shutil
import os


def create():
    try:
        directory = name.get()
        path = filedialog.askdirectory()
        os.mkdir(path+'/'+directory)
    except Exception as error:
        messagebox.showerror("Ошибка", str(error))


root = Tk()  # создаем корневой объект - окно
root.title("КР 1")  # устанавливаем заголовок окна
root.geometry("400x100")  # устанавливаем размеры окна
root.resizable(False, False)

Info = Label(text="Введите название папки")  # создаем текстовую метку
Info.pack()
name = ttk.Entry()
name.pack()
btn = ttk.Button(text="Создать папку в выбранной папке", command=create)
btn.pack()

root.mainloop()
