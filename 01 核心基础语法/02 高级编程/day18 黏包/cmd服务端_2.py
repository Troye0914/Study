import socket
import struct
import subprocess

'''
因为客户端不清楚接收的数据长度
让服务端在发送数据时，先发送数据长度（固定报头）
客户端可以先读取报头，准备循环接收数据
'''

cmd_tel = socket.socket()
cmd_tel.bind(('127.0.0.1', 10099))
cmd_tel.listen(5)
conn, adder = cmd_tel.accept()

while True:
    try:
        # 接收到客户端要查询cmd指令
        cmd = conn.recv(1024)
        # 获取到cmd指令的查询结果
        # 获得到的数据不可以直接进入cmd查询，需要进行解码
        obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                               stdout=subprocess.PIPE,  # 获取指令正确的结果
                               stderr=subprocess.PIPE)
        stdout = obj.stdout.read()  # 获取指令正确的结果
        stderr = obj.stderr.read()  # 获取指令错误的结果
        # 因为不让黏包发生，先发送数据长度
        size = len(stdout) + len(stderr)
        # 制作数据报头
        header = struct.pack('i', size)
        # 在发送数据之前，先发送数据报头
        conn.send(header)
        # 因为服务端不指定客户端的指令是否正确，所以将两个返回结果一起发送
        conn.send(stdout + stderr)
    except Exception:
        break

conn.close()
cmd_tel.close()
