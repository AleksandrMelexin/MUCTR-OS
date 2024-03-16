import tkinter as tk
from threading import Thread
from second import Counter
# приложение имеет 2 счётчика, работающих в разных потоках, счётчик с низким приоритетом увеличивается на 1 за 1 секунду, а счётчик с высоким приоритетом на 2 за 1 секунду
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("lab5")
        self.geometry("150x150")
        self.resizable(False, False)

        self.counter1 = Counter(self, priority=2)  # Высокий приоритет по умолчанию
        self.counter1.grid(row=0, column=0, padx=10, pady=10)

        self.counter2 = Counter(self, priority=1)  # Низкий приоритет по умолчанию
        self.counter2.grid(row=1, column=0, padx=10, pady=10)

        self.btn_change_priority = tk.Button(self, text="Изменить приоритет", command=self.change_priority)
        self.btn_change_priority.grid(row=2, column=0, padx=10, pady=10)

    def change_priority(self):
        self.counter1.toggle_priority()
        self.counter2.toggle_priority()

if __name__ == "__main__":
    app = App()
    app.mainloop()