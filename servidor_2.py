import socket

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Aguardando conexão de um cliente")
conn, ender = s.accept()

print(f"Conectado em {ender}")
while True:
    data = conn.recv(1024)
    if not data:
        print("Conexão encerrada")
        break
    conn.sendall(data)