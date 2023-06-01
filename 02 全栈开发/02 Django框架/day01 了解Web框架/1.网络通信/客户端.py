import socket


client = socket.socket()
client.connect(('127.0.0.1', 8098))

while True:
    msg = input('>>>')
    if not msg: continue
    if msg == 'q': break
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))
