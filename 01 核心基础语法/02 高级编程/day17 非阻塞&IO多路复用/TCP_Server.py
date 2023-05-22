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
print('没人连接')
conn, adder = phone.accept()
print('有人来啦')

# 5.接受客户端的数据/给客户端发送数据
while True:
    try:
        print('没人聊天')
        data = conn.recv(1024)
        print('聊天中')
        if not data:
            break
        print(data.decode('utf-8'))
        conn.send(data)
    except ConnectionResetError:
        break

# 6.关闭连接
conn.close()
phone.close()
