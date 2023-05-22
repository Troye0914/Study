import socket

server = socket.socket()
server.bind(('127.0.0.1', 10086))
server.listen(5)

# 一直响应
while True:
    sock, adder = server.accept()
    data = sock.recv(1024)
    # 发送响应数据
    '''
    网页响应数据需要遵循http协议，超文本传输协议，用来规定服务端和浏览器之间的数据交互格式
    如果不遵守http协议，该服务端的数据是无法正常被浏览器响应出来，不遵守就只能自己写一个客户端进行数据接收

    数据响应格式
    1.响应首行（标识http协议的版本，响应状态码200表示响应成功）
    2.响应头(一大堆键值对）
    3.\r\n
    4.响应体（返回给浏览器展示给用户看的数据）
    
    请求数据格式
    1.请求首行（标识http协议的版本，数据请求格式[get，post]）
    2.请求头(一大堆键值对）
    3.\r\n
    4.请求体（获得数据，并不是所有请求都可以获得数据）
    '''
    # 让浏览器响应我们的数据，发送一个http协议
    sock.send('HTTP1.1 200 OK \r\n\r\n'.encode('utf-8'))
    sock.send('hello world'.encode('utf-8'))
