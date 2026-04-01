import socket

HOST = 'localhost'
PORT = 50007

login = input("Логин: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(f"LOGIN:{login}".encode('utf-8'))

while True:
    msg = input("Сообщение (end для выхода): ")
    if msg == "end":
        break
    s.sendall(f"MSG:{msg}".encode('utf-8'))

s.close()