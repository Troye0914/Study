import socket
import struct

'''
先获取数据报头
根据数据报头来循环接收数据
最后把每次循环得到的数据进行拼接
'''

phone = socket.socket()
phone.connect(('127.0.0.1', 10099))

while True:
    # 输入指令
    msg = input('>>>')
    if msg == 'q': break
    if not msg: continue
    phone.send(msg.encode('utf-8'))

    # 接收数据
    # 1.获取到服务端发送的数据报头
    header = phone.recv(4)
    # 2.将获取到的字节报头进行转码，切取出想要的数据
    size = struct.unpack('i', header)[0]
    # 记录每次循环接收到的字节个数
    recv_size = 0
    # 将每次循环接收的数据进行拼接
    # b''表示字节类型
    recv_data = b''
    # 当接收到的数据长度小于要接收的数据长度，那么就继续循环接收
    # 若超过了，则表示接收完毕
    while recv_size < size:
        # 接收数据
        data = phone.recv(1024)
        # 进行数据拼接
        recv_data += data
        # 累加循环接收到的字节个数
        recv_size += len(data)
    print(recv_data.decode('gbk'))

phone.close()
