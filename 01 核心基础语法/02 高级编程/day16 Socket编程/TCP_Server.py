# 通过socket创建服务端流程
import socket

# 1.创建服务端socket对象
'''
socket.socket：没有写参数，默认是tcp协议套接字
socket_family 网络地址类型 AF_INET 表示的是ipv4 地址类型
socket_type 套接字类型，使用的是网络相同协议
            SOCK_STREAM：表示的是tcp协议套接字
            SOCK_DGRAM：表示的是udp协议套接字
'''
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.绑定自己的ip以及端口号（动态端口号：1204-65535）
'''
bind的参数必须是一个元组类型
这个元组的元素就是(ip, port)
port端口号使用的是动态端口号1024-65535之间
'''
phone.bind(('127.0.0.1', 10086))

# 3.设置监听模式，设置最大连接数
phone.listen(5)

# 4.等待客户端连接
'''
accept 这个方法是有返回值，并且是有两个返回值
        1.客户端连接的socket对象，我们后续数据的接受和发送都是要使用这个对象
        2.连接的客户端的ip地址以及端口号
'''
conn, adder = phone.accept()

# 添加循环进行无限的接收发送消息
while True:
    # 当客户端关闭了，服务端会报ConnectionResetError
    try:
        # 5.接受客户端的数据/给客户端发送数据
        # 接受数据，recv的参数表示接收最大的字节数
        data = conn.recv(1024)
        # 得到的数据：b'\xe9\x98\xbf\xe5\xae\xb8\xe7\x9c\x9f\xe5\xb8\x85'
        # 只能发送二进制数据，所以接收数据的时候需要进行解码操作 decode()
        print(data.decode('utf-8'))
        # 发送消息
        msg = input('>>>')
        conn.send(msg.encode('utf-8'))
    except ConnectionResetError:
        break

# 6.关闭连接
conn.close()
phone.close()
