import socket
import tkinter as tk
from tkinter import messagebox

HOST = 'localhost'
PORT = 50007

sock = None
connected = False

def send_message():
    global sock, connected

    login = entry_login.get().strip()
    msg = entry_msg.get().strip()

    if not login:
        messagebox.showwarning("Ошибка", "Введите логин")
        return
    if not msg:
        return

    try:
        if not connected:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            sock.sendall(f"LOGIN:{login}".encode('utf-8'))
            connected = True

        sock.sendall(f"MSG:{msg}".encode('utf-8'))
        entry_msg.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Ошибка сети", str(e))

def on_close():
    global sock
    try:
        if sock:
            sock.close()
    except:
        pass
    root.destroy()

root = tk.Tk()
root.title("Чат-клиент")

tk.Label(root, text="Логин:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_login = tk.Entry(root, width=30)
entry_login.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Сообщение:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_msg = tk.Entry(root, width=30)
entry_msg.grid(row=1, column=1, padx=5, pady=5)

btn_send = tk.Button(root, text="Отправить", command=send_message)
btn_send.grid(row=2, column=0, columnspan=2, pady=10)

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()