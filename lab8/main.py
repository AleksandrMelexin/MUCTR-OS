import tkinter as tk
from tkinter import ttk
import pyautogui


class WindowApp:
    def __init__(self, root):        
        self.root = root
        self.root.title("lab8")
        self.root.geometry("400x300")
        self.root.resizable(False, False) 
        
        self.label = tk.Label(root, text="Список открытых окон")
        self.label.grid(row=0, column=0, columnspan=4)

        self.table = ttk.Treeview(root, columns=('№', 'Окно'), show='headings')
        self.table.heading('№', text='№')
        self.table.heading('Окно', text='Окно')
        self.table.grid(row=1, column=0, columnspan=4)

        self.button_close = tk.Button(root, text="Закрыть окно", command=self.close_window)
        self.button_close.grid(row=3, column=0)

        self.button_info = tk.Button(root, text="Получить информацию")
        self.button_info.grid(row=3, column=1)
        self.windows = {}
        self.get_windows()
        
    def close_window(self):
            selected_item = self.table.selection()
            if selected_item:  
                item = self.table.item(selected_item[0])  
                index = item['values'][0]  
                window = self.windows[index]
                window.close()
                self.get_windows()
            
    def clear_table(self):
        self.windows.clear()
        for row in self.table.get_children():
            self.table.delete(row)      
                
    def get_windows(self):
        self.clear_table()
        number = 1
        for window in pyautogui.getAllWindows():  
            if window.title != "":
                self.windows[number] = window
                self.table.insert("", tk.END, values=[number, window.title])
                number += 1
                                

if __name__ == "__main__":
    root = tk.Tk()
    app = WindowApp(root)
    root.mainloop()