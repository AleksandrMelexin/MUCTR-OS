import socket
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import netifaces

clients = {}
usernames = set()
server_running = False

def handle_client(client_socket, addr):
    global usernames
    try:
        username = client_socket.recv(1024).decode('utf-8')
        if username in usernames:
            client_socket.send("Имя пользователя уже занято!".encode('utf-8'))
            client_socket.close()
            return
        else:
            client_socket.send("OK".encode('utf-8'))
            usernames.add(username)
            clients[client_socket] = username
            update_client_list()

        broadcast(f"{username} присоединился к чату!".encode('utf-8'), client_socket)

        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
    except:
        pass
    finally:
        if client_socket in clients:
            broadcast(f"{clients[client_socket]} покинул чат.".encode('utf-8'), client_socket)
            usernames.remove(clients[client_socket])
            del clients[client_socket]
            update_client_list()
            client_socket.close()

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                del clients[client]

def get_local_ip():
    for interface in netifaces.interfaces():
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            for addr in addresses[netifaces.AF_INET]:
                ip = addr['addr']
                if ip.startswith('192.168.'):
                    return ip
    return '127.0.0.1'

def start_server():
    global server, server_running
    if not server_running:
        server_running = True
        threading.Thread(target=run_server).start()
        start_button.config(state=tk.DISABLED)

def run_server():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen(5)

    local_ip = get_local_ip()
    server_ip_label.config(text=f"Сервер запущен на IP: {local_ip}, порт: 5555")

    while server_running:
        try:
            client_socket, addr = server.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_handler.start()
        except OSError:
            break

def update_client_list():
    user_listbox.delete(0, tk.END)
    for username in usernames:
        user_listbox.insert(tk.END, username)

def on_closing():
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Сервер чата")

    server_ip_label = tk.Label(root, text="Сервер не запущен")
    server_ip_label.pack(pady=10)

    start_button = tk.Button(root, text="Запустить сервер", command=start_server)
    start_button.pack(pady=5)

    user_listbox = tk.Listbox(root, height=10, width=50)
    user_listbox.pack(pady=10)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()