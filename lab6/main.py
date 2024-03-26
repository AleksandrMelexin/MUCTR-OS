import tkinter as tk
import ctypes
import os


def call_dll_function():
    # Загружаем dll файл
    os.add_dll_directory(os.getcwd())
    my_dll = ctypes.CDLL('my_dll.dll')

    # Вызываем функцию из dll файла
    new_text = my_dll.my_function()
    label.config(text=new_text)


app = tk.Tk()
app.title("lab6")
app.geometry("200x200")
app.resizable(False, False)

button = tk.Button(app, text="Call DLL Function", command=call_dll_function)
button.pack()

label = tk.Label(app, text="")
label.pack()

app.mainloop()