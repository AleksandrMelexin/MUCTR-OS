import tkinter as tk
from threading import Thread
import time

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Главное окно")
        self.geometry("300x75")
        self.resizable(False, False)
        self.label = tk.Label(self, text="Ожидание...")
        self.label.pack(pady=20)
        
        # Запускаем второй поток
        thread = SecondThread(self)
        thread.start()

    def update_label(self, text):
        self.label.config(text=text)

class SecondThread(Thread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
    def run(self):
        while True:
            self.main_window.update_label("Второй поток: работает...")
            time.sleep(1)
            self.main_window.update_label("Второй поток: продолжает работу...")
            time.sleep(1)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()