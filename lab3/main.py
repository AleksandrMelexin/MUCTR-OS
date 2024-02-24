from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import shutil

root = Tk()
root.title("lab3")
root.geometry("400x400")


def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        os.remove(filepath)


# сохраняем текст из текстового поля в файл
def rename_file():
    filepath = filedialog.askopenfilename()
    name = new_name.get()  # новое имя файла
    path = filepath[:filepath.rfind("/") + 1]
    extension = filepath[filepath.rfind("."):]  # расширение файла
    if filepath != "" and name != "":
        os.rename(filepath, path + name + extension)
    new_name.delete(0, END)


def replace_file():
    old_path = filedialog.asksaveasfilename()
    if filepath != "":
        new_path = filedialog.askdirectory()
        name = old_path[old_path.rfind("/"):]
        shutil.move(old_path, new_path + name)


delete_button = ttk.Button(text="Удалить файл", command=open_file)
delete_button.pack()
label = Label(text="Введите новое имя для файла")
label.pack()
new_name = ttk.Entry()
new_name.pack()
rename_button = ttk.Button(text="Переименовать файл", command=rename_file)
rename_button.pack()
replace_button = ttk.Button(text="Переместить файл", command=rename_file)
replace_button.pack()

root.mainloop()
