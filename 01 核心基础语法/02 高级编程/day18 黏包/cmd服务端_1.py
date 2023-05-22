import socket
import subprocess

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
        # 因为服务端不指定客户端的指令是否正确，所以将两个返回结果一起发送
        conn.send(stdout + stderr)
    except Exception:
        break

conn.close()
cmd_tel.close()
