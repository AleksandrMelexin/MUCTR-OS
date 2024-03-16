import tkinter as tk
from threading import Thread
import time

class Counter(tk.Label):
    def __init__(self, master, priority):
        super().__init__(master, text="0", font=("Helvetica", 16))

        self.priority = priority
        self.running = True

        self.thread = Thread(target=self.count)
        self.thread.daemon = True
        self.thread.start()

    def count(self):
        while self.running:
            if self.priority == 2:
                self.increment(2)
            else:
                self.increment(1)
            time.sleep(1)

    def increment(self, value):
        current_value = int(self["text"])
        self["text"] = str(current_value + value)

    def toggle_priority(self):
        self.priority = 3 - self.priority  # Переключение между счётчиками