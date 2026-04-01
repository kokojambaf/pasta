import socket

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = input("Введите сообщение (end для выхода): ")
    if msg == "end":
        break
    s.sendall(msg.encode('utf-8'))

s.close()