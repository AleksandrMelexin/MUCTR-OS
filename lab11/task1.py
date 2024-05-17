import tkinter as tk
from tkinter import filedialog, messagebox
import ctypes
import platform

class AppLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("App Launcher")
        self.geometry("400x200")
        
        self.label = tk.Label(self, text="Выберите файл или приложение для запуска")
        self.label.pack(pady=10)
        
        self.file_path = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.file_path, width=50)
        self.entry.pack(pady=10)
        
        self.browse_button = tk.Button(self, text="Обзор", command=self.browse_file)
        self.browse_button.pack(pady=5)
        
        self.launch_button = tk.Button(self, text="Запустить", command=self.launch_app)
        self.launch_button.pack(pady=5)
    
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)
    
    def launch_app(self):
        file_path = self.file_path.get()
        if file_path:
            try:
                if platform.system() == 'Windows':
                    # Использование ShellExecute для Windows
                    ctypes.windll.shell32.ShellExecuteW(None, "open", file_path, None, None, 1)
                else:
                    messagebox.showerror("Ошибка", "Эта функция поддерживается только на Windows.")
                messagebox.showinfo("Успех", "Приложение/файл успешно запущен")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось запустить приложение/файл: {e}")
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите файл или приложение для запуска")

if __name__ == "__main__":
    app = AppLauncher()
    app.mainloop()