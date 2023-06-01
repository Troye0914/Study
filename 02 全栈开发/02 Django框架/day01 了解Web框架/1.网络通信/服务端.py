import socket


server = socket.socket()
server.bind(('127.0.0.1', 8098))
server.listen(5)

while True:
    sock, address = server.accept()
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    sock.send(data)
