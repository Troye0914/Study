import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 10087)
while True:
    # 发送数据
    msg = input('>>>')
    if msg == 'q':
        break
    phone.sendto(msg.encode('utf-8'), ip_port)
    # 接收数据
    data, adder = phone.recvfrom(1024)
    print(data.decode('utf-8'))
