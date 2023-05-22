import socket

phone = socket.socket()
phone.connect(('127.0.0.1', 10099))

while True:
    # 输入指令
    msg = input('>>>')
    if msg == 'q': break
    if not msg: continue
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)
    print(data.decode('gbk'))

phone.close()
