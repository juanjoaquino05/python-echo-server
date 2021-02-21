import socket

ip='127.0.0.1'
port=5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((ip, port))
    client.sendall(b'testing\r\n')
    data = client.recv(1024)

print(repr(data))