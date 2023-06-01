import socket


server = socket.socket()  # 默认是TCP协议
server.bind(('127.0.0.1', 8100))
server.listen(5)


# 把不同的url响应的数据封装成函数
def index(url):
    return bytes(f'我是{url}响应的页面数据', encoding='gbk')


def ac(url):
    return bytes('阿宸好帅', encoding='gbk')


# 把url以及对应功能函数用字典进行对应关系
url_dict = {
        '/index/': index,
        '/ac/': ac
    }

while True:
    """
    http协议数据响应的格式
    1.响应首行（http协议的版本 响应状态码）
    2.响应头（一些键值对）
    3.空行 \r\n
    4.响应体返回给浏览器展示给用户看的数据
    """
    sock, address = server.accept()
    data = sock.recv(1024).decode('utf-8')
    # 浏览器发送的http协议请求
    print(data)
    url = data.split(' ')[1]
    # 以http协议发送响应数据 前提就是先发送一个http协议
    sock.send(b'HTTP1.1 200 OK \r\n\r\n')
    # 定义一个变量作为程序的标志
    msg = 1
    # 循环遍历url对应关系的字典
    for i in url_dict:
        # 判断获取到到数据是否等于请求的url
        if i == url:
            # 调用url对应的功能函数
            func = url_dict[i](url)
            sock.send(func)
            msg = 0
    # 判断是否有对应url响应数据
    if msg:
        sock.send('404 not found'.encode('utf-8'))
