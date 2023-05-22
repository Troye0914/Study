# 服务端
import socket

# 1.创建服务端socket对象
phone = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2.绑定自己的ip以及端口号（动态端口号：1204-65535）
phone.bind(('127.0.0.1', 10087))

while True:
    # 3.接受客户端的数据/给客户端发送数据
    # 接受数据，recv的参数表示接收最大的字节数
    '''
    recvfrom：这个方法有两个返回值：
            1.客户端连接的套接字对象（客户端发送过来的数据）
            2.客户端的ip地址与端口号
    '''
    data, adder = phone.recvfrom(1024)
    print(data.decode('utf-8'))
    print(adder)
    # 发送消息 sendto(要发送的数据，对方的ip与端口号)
    phone.sendto(data, adder)
