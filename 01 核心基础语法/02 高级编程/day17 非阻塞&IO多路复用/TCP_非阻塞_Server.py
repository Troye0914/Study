# 通过socket创建服务端流程
import socket

# 1.创建服务端socket对象
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.绑定自己的ip以及端口号（动态端口号：1204-65535）
phone.bind(('127.0.0.1', 10086))
# 设置socket非阻塞状态
phone.setblocking(False)

# 3.设置监听模式，设置最大连接数
phone.listen(5)
# 保存客户端的socket对象
r_list = []
while True:
    try:
        # 4.等待客户端连接
        conn, adder = phone.accept()
        # 有客户端连接，就保存客户端的对象
        r_list.append(conn)
    except BlockingIOError:
        # 当accept发生阻塞时，执行这里面的内容
        # 客户端对象从r_list中遍历出来
        for i in r_list:
            try:
                # 5.接受客户端的数据/给客户端发送数据
                data = i.recv(1024)
                if not data:
                    break
                print(data.decode('utf-8'))
                i.send(data)
            except BlockingIOError:
                # 接收消息发生阻塞，跳过该客户端对象，访问另一个对象
                continue
            except ConnectionResetError:
                # 客户端关机
                i.close()
                r_list.remove(i)

# 6.关闭连接
phone.close()
