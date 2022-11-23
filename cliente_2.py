import socket 

HOST = "127.0.0.1"
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORT))
mensagem  = input("Digite a mensagem a ser enviada")
s.sendall(str.encode(mensagem))
data = s.recv(1024)

print(f"Mensagem ecoada: {data.decode()}")