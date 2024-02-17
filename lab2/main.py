from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import psutil  # нужно прописать pip install psutil
import os


def main():
    root = Tk()  # создаем корневой объект - окно
    root.title("lab2")  # устанавливаем заголовок окна
    root.geometry("200x200")  # устанавливаем размеры окна
    root.resizable(False, False)

    # получаем имена и типы дисков
    names = []
    types = []
    DiskInfo = psutil.disk_partitions(all=False)  # полученине информации о дисках
    for disk in DiskInfo:
        names.append(disk[0])
        types.append(disk[2])
        names[-1] = names[-1][:-1]
    # считываем память дисков
    memories = []
    for name in names:
        memories.append(psutil.disk_usage(name))
    s = ""
    for i in range(len(names)):
        # print("Имя диска:", names[i])
        s += "Имя диска: " + names[i] + " \n"
        # print("Тип:", types[i])
        s += "Тип: " + types[i] + " \n"
        # print("Всего места:", round(memories[i][0] / (1024 ** 3), 2))
        s += "Всего места: " + str(round(memories[i][0] / (1024 ** 3), 2)) + " \n"
        # print("Свободно места:", round(memories[i][2] / (1024 ** 3), 2))
        s += "Свободно места: " + str(round(memories[i][2] / (1024 ** 3), 2)) + " \n"
        # print("------------------------")
        s += "------------------------\n"
    diskInfo = Label(text=s)  # создаем текстовую метку
    diskInfo.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
