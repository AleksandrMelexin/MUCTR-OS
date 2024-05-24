import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog

class Client:
    def __init__(self, root):
        self.root = root
        self.root.title("Чат Клиента")

        self.server_ip = simpledialog.askstring("Сервер IP", "Пожалуйста, введите IP адрес сервера:")
        if not self.server_ip:
            self.root.destroy()
            return

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.server_ip, 5555))
        except ConnectionRefusedError:
            messagebox.showerror("Ошибка", "Не удается подключиться к серверу.")
            self.root.destroy()
            return

        self.name = self.prompt_for_name()
        if not self.name:
            self.root.destroy()
            return

        self.messages = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.messages.pack(padx=20, pady=5)
        self.messages.config(state=tk.DISABLED)

        self.entry_message = tk.Entry(root, width=50)
        self.entry_message.pack(padx=20, pady=5)
        self.entry_message.bind("<Return>", self.send_message)

        self.button_send = tk.Button(root, text="Отправить", command=self.send_message)
        self.button_send.pack(padx=20, pady=5)

        self.receive_thread = threading.Thread(target=self.receive_message)
        self.receive_thread.start()

    def prompt_for_name(self):
        while True:
            name = simpledialog.askstring("Имя", "Пожалуйста, введите ваше имя:")
            if not name:
                return None
            self.client_socket.send(name.encode('utf-8'))
            response = self.client_socket.recv(1024).decode('utf-8')
            if response == "OK":
                return name
            else:
                messagebox.showerror("Ошибка", "Имя пользователя уже занято. Пожалуйста, выберите другое имя.")

    def send_message(self, event=None):
        message = self.entry_message.get()
        if message:
            full_message = f"{self.name}: {message}"
            self.client_socket.send(full_message.encode('utf-8'))
            self.display_message("Вы: " + message)
            self.entry_message.delete(0, tk.END)

    def display_message(self, message):
        self.messages.config(state=tk.NORMAL)
        self.messages.insert(tk.END, message + "\n")
        self.messages.config(state=tk.DISABLED)
        self.messages.yview(tk.END)

    def receive_message(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.display_message(message)
            except ConnectionAbortedError:
                break
            except:
                messagebox.showerror("Ошибка", "Произошла ошибка!")
                break

if __name__ == "__main__":
    root = tk.Tk()
    client = Client(root)
    root.mainloop()
