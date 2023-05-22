# 客户端
import socket

# 1.创建客户端socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.连接服务端的ip与端口号
# ip与端口号要与被连接的服务端一致
client.connect(('127.0.0.1', 10086))

# 添加循环进行无限的接收发送消息
while True:
    # 3.接收服务端的数据/给服务端发送数据
    # 发送消息，发送的数据是一个二进制数据，进行转码——encode()
    # tcp套接字不允许发送空白消息
    msg = input('>>>')
    client.send(msg.encode('utf-8'))
    # 设置退出
    if msg == 'q':
        break
    # 判断消息是否为空
    if not msg:
        break
    # 接收消息
    data = client.recv(1024)
    print(data.decode('utf-8'))

# 4.关闭
client.close()
