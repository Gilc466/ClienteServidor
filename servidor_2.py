import socket

HOST = '192.168.2.107'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Aguardando conexão de um cliente")
conn, ender = s.accept()

print(f"Conectado em {ender}")

while True:
    data = conn.recv(1024)
    if data:
        print(f"Mensagem enviada de cliente: {data.decode()}")
    else:
        print("Conexão encerrada")
        break
    conn.sendall(data)