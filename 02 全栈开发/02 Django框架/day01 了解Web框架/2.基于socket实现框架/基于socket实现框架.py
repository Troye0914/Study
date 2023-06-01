import socket

server = socket.socket()    # 默认是TCP协议
server.bind(('127.0.0.1',8098))
server.listen(5)

while True:
    '''
    127.0.0.1 发送的响应无效 : 就是客户端与服务端之间遵循的协议不同。
    我们自己的服务端必须遵循http协议的数据传输 ， 否则浏览器无法响应到数据
    
    http协议数据响应的格式
    1、响应首行(http协议的版本 ， 响应状态码)200 OK
    2、响应头：是一些键值对
    3、空行 ： \r\n
    4、响应体：返回给浏览器展示给用户看的数据
    '''
    sock , address  = server.accept()
    data = sock.recv(1024).decode('utf-8')
    # 浏览器发送的http协议请求
    print(data)
    url = data.split(' ')[1]
    # 以http协议发送响应数据 ， 前提就是先发送一个http协议
    sock.send(b'HTTP1.1 200 OK \r\n\r\n')
    # 响应数据
    if url == '/index/':
        sock.send(b'hello world')
    elif url == '/ac/':
        sock.send('阿宸好帅'.encode('gbk'))
    else:
        sock.send('404'.encode('utf-8'))

