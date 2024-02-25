import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Файловый Менеджер (lab3)")

        self.create_widgets()

    def create_widgets(self):
        # Фрейм для кнопок
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Кнопка "Переместить файл"
        self.move_button = tk.Button(self.button_frame, text="Переместить файл", command=self.move_file)
        self.move_button.grid(row=0, column=0, padx=5)

        # Кнопка "Скопировать файл"
        self.copy_button = tk.Button(self.button_frame, text="Скопировать файл", command=self.copy_file)
        self.copy_button.grid(row=0, column=1, padx=5)

        # Кнопка "Переименовать файл"
        self.rename_button = tk.Button(self.button_frame, text="Переименовать файл", command=self.rename_file)
        self.rename_button.grid(row=0, column=2, padx=5)

        # Кнопка "Удалить файл"
        self.delete_button = tk.Button(self.button_frame, text="Удалить файл", command=self.delete_file)
        self.delete_button.grid(row=0, column=3, padx=5)

    def ask_file_path(self):
        file_path = filedialog.askopenfilename()
        return file_path

    def move_file(self):
        src_file = self.ask_file_path()
        if src_file:
            dest_folder = filedialog.askdirectory()
            if dest_folder:
                try:
                    shutil.move(src_file, dest_folder)
                    messagebox.showinfo("Успех", "Файл успешно перемещен!")
                except Exception as e:
                    messagebox.showerror("Ошибка", str(e))

    def copy_file(self):
        src_file = self.ask_file_path()
        if src_file:
            dest_folder = filedialog.askdirectory()
            if dest_folder:
                try:
                    shutil.copy(src_file, dest_folder)
                    messagebox.showinfo("Успех", "Файл успешно скопирован!")
                except Exception as e:
                    messagebox.showerror("Ошибка", str(e))

    def rename_file(self):
        src_file = self.ask_file_path()
        if src_file:
            dest_file = filedialog.asksaveasfilename()
            if dest_file:
                try:
                    os.rename(src_file, dest_file)
                    messagebox.showinfo("Успех", "Файл успешно переименован!")
                except Exception as e:
                    messagebox.showerror("Ошибка", str(e))

    def delete_file(self):
        src_file = self.ask_file_path()
        if src_file:
            try:
                os.remove(src_file)
                messagebox.showinfo("Успех", "Файл успешно удален!")
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
