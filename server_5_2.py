import socket
from datetime import datetime

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:  # постоянное прослушивание подключений
    conn, addr = s.accept()
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            text = data.decode('utf-8')
            now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
            print(f"{now} ({addr[0]}:{addr[1]}): {text}")
    finally:
        conn.close()