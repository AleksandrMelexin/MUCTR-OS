from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def calculate():
    string = entry.get()
    if string != '':
        try:
            x = int(string)
            answer["text"] = 'ответ: ' + str(x * x - 3 + x)
        except:
            messagebox.showerror('Ошибка', 'Были введены некорректные данные!')
    entry.delete(0, END)


root = Tk()  # создаем корневой объект - окно
root.title("Задание 1")  # устанавливаем заголовок окна
root.geometry("400x100")  # устанавливаем размеры окна
root.resizable(False, False)

label = Label(text="Введите целое число")  # создаем текстовую метку
answer = Label(text="Ответ:")
entry = ttk.Entry()
btn = ttk.Button(text="Вычислить", command=calculate)
label.pack()  # размещаем метку в окне
entry.pack()
btn.pack()
answer.pack()

root.mainloop()
