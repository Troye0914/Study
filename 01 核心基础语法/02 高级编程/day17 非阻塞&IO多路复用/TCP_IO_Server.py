import socket
import select

tel = socket.socket()
tel.bind(('192.168.3.46', 10088))
tel.listen(5)
tel.setblocking(False)

# 保存socket对象，[第一个数据是服务端自己的socket对象]
# 在监听的时候，判断是否可读，可读时表示有客户端进行连接
r_list = [tel]

while True:
    # 监控io，检测阻塞情况
    # 返回的第一个参数是可读的对象连接列表
    read_list, w, e = select.select(r_list, [], [])
    # 遍历select返回的可读对象列表
    for read in read_list:
        # 获取自己服务端的socket对象，进行连接客户端
        if read is tel:
            # 进行接收与客户端连接
            conn, adder = read.accept()
            # 把客户端对象保存到列表中进行监控
            r_list.append(conn)
        else:
            try:
                # 可读连接并不是自己服务端的对象
                # 进行消息接收与发送
                data = read.recv(1024)
                print(data.decode('utf-8'))
                read.send(data)
            except Exception:
                read.close()
                r_list.remove(read)
                continue
