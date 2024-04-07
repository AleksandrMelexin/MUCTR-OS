import tkinter as tk
from tkinter import ttk

class WindowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер окон")
        self.root.geometry("600x400")  # Установка статического размера окна
        
        self.label = tk.Label(root, text="Список открытых окон")
        self.label.grid(row=0, column=0, columnspan=4)

        self.table = ttk.Treeview(root, columns=('№', 'Окно'), show='headings')
        self.table.heading('№', text='№')
        self.table.heading('Окно', text='Окно')
        self.table.grid(row=1, column=0, columnspan=4)

        self.button_left = tk.Button(root, text="Влево")
        self.button_left.grid(row=2, column=0)

        self.button_right = tk.Button(root, text="Вправо")
        self.button_right.grid(row=2, column=1)

        self.button_down = tk.Button(root, text="Вниз")
        self.button_down.grid(row=2, column=2)

        self.button_up = tk.Button(root, text="Вверх")
        self.button_up.grid(row=2, column=3)

        self.button_close = tk.Button(root, text="Закрыть окно")
        self.button_close.grid(row=3, column=0)

        self.button_info = tk.Button(root, text="Получить информацию", command=self.get_selected_item)
        self.button_info.grid(row=3, column=1)

        self.button_delete = tk.Button(root, text="Удалить файл", command=self.clear_table)
        self.button_delete.grid(row=3, column=2)

        # Пример добавления данных при инициализации
        self.insert_data([("1", "Окно 1"), ("2", "Окно 2"), ("3", "Окно 3")])

    def clear_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

    def insert_data(self, data):
        for item in data:
            self.table.insert('', 'end', values=item)

    def get_selected_item(self):
        selected_item = self.table.selection()  # Получаем выбранный элемент
        if selected_item:  # Если элемент выбран
            item = self.table.item(selected_item[0])  # Получаем информацию о выбранном элементе
            print(item['values'])  # Выводим значения элемента

if __name__ == "__main__":
    root = tk.Tk()
    app = WindowApp(root)
    root.mainloop()