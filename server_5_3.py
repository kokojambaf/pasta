import socket
from datetime import datetime

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    conn, addr = s.accept()
    login = "unknown"

    try:
        first = conn.recv(1024)
        if not first:
            conn.close()
            continue

        first_text = first.decode('utf-8')
        if first_text.startswith("LOGIN:"):
            login = first_text[6:]
        print(f"подключился {login}")

        while True:
            data = conn.recv(1024)
            if not data:
                break
            text = data.decode('utf-8')

            if text.startswith("MSG:"):
                msg = text[4:]
            else:
                msg = text

            now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
            print(f"{now} {login}: {msg}")

    finally:
        conn.close()