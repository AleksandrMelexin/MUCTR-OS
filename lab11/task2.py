# проверка
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import subprocess
import threading
import os

class VideoConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер Видео")
        self.root.geometry("510x200")
        self.root.resizable(False, False) 
        # Поле для выбора входного файла
        self.input_file_label = tk.Label(self.root, text="Выбрать файл:")
        self.input_file_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')
        
        self.input_file_entry = tk.Entry(self.root, width=50)
        self.input_file_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        
        self.browse_input_button = tk.Button(self.root, text="Обзор", command=self.browse_input_file)
        self.browse_input_button.grid(row=0, column=2, padx=10, pady=5)
        
        # Поле для выбора выходного файла
        self.output_file_label = tk.Label(self.root, text="Сохранить в:")
        self.output_file_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        
        self.output_file_entry = tk.Entry(self.root, width=50)
        self.output_file_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        
        self.browse_output_button = tk.Button(self.root, text="Обзор", command=self.browse_output_file)
        self.browse_output_button.grid(row=1, column=2, padx=10, pady=5)
        
        # Выбор формата
        self.format_label = tk.Label(self.root, text="Формат:")
        self.format_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        
        self.format_var = tk.StringVar(self.root)
        self.format_var.set("mp4")  # формат по умолчанию
        
        self.format_menu = ttk.Combobox(self.root, textvariable=self.format_var, values=["mp4", "avi", "mov", "mkv"])
        self.format_menu.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        
        # Кнопка конвертации
        self.convert_button = tk.Button(self.root, text="Конвертировать", command=self.start_conversion)
        self.convert_button.grid(row=3, column=1, padx=10, pady=10)
        
        # Полоса прогресса
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.progress.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    
    def browse_input_file(self):
        input_file = filedialog.askopenfilename(title="Выберите входной видеофайл", filetypes=[("Все файлы", "*.*"), ("MP4 файлы", "*.mp4"), ("AVI файлы", "*.avi"), ("MOV файлы", "*.mov"), ("MKV файлы", "*.mkv")])
        if input_file:
            self.input_file_entry.delete(0, tk.END)
            self.input_file_entry.insert(0, input_file)
    
    def browse_output_file(self):
        output_format = self.format_var.get()
        output_file = filedialog.asksaveasfilename(title="Выберите выходной видеофайл", defaultextension=f".{output_format}", filetypes=[(f"{output_format.upper()} файлы", f"*.{output_format}")])
        if output_file:
            self.output_file_entry.delete(0, tk.END)
            self.output_file_entry.insert(0, output_file)
    
    def start_conversion(self):
        input_file = self.input_file_entry.get()
        output_file = self.output_file_entry.get()
        
        if not input_file or not output_file:
            messagebox.showerror("Ошибка", "Пожалуйста, выберите входной и выходной файлы.")
            return
        
        self.progress["value"] = 0
        self.convert_button["state"] = "disabled"
        
        # Запуск конвертации в новом потоке
        threading.Thread(target=self.convert_video, args=(input_file, output_file)).start()
    
    def convert_video(self, input_file, output_file):
        command = [
            "ffmpeg",
            "-i", input_file,
            output_file
        ]
        
        # Запуск команды ffmpeg и получение процесса
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        
        duration = None
        # Обработка вывода по строкам для обновления полосы прогресса
        for line in process.stdout:
            if "Duration" in line:
                duration = self.extract_duration(line)
            if "time=" in line:
                time = self.extract_time(line)
                if duration and time:
                    progress = (time / duration) * 100
                    self.update_progress(progress)
        
        process.wait()
        self.update_progress(100)
        self.convert_button["state"] = "normal"
        messagebox.showinfo("Успех", "Конвертация видео завершена.")
    
    def extract_duration(self, line):
        duration_str = line.split("Duration:")[1].split(",")[0].strip()
        h, m, s = duration_str.split(':')
        return int(h) * 3600 + int(m) * 60 + float(s)
    
    def extract_time(self, line):
        time_str = line.split("time=")[1].split(" ")[0].strip()
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + float(s)
    
    def update_progress(self, progress):
        self.progress["value"] = progress
        self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoConverterApp(root)
    root.mainloop()