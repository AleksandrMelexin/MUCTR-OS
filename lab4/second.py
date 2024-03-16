import tkinter as tk
from threading import Thread
import time

class HelperThread(Thread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
    def run(self):
        while True:
            self.main_window.update_label("Вспомогательный поток: работает...")
            time.sleep(2)
            self.main_window.update_label("Вспомогательный поток: продолжает работу...")
            time.sleep(2)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Скрываем окно вспомогательного приложения
    app = HelperThread(root)
    app.start()
    root.mainloop()