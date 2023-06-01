from wsgiref.simple_server import make_server


# 把不同的url响应的数据封装成函数
def index(url):
    # 服务器响应前端页面
    with open('index.html', 'r', encoding='utf-8') as f:
        data = f.read()
    # 将读取出来的页面数据返回给浏览器
    return bytes(data.encode('utf-8'))


def ac(url):
    return bytes('阿宸好帅', encoding='gbk')


# 把url以及对应功能函数用字典进行对应关系
url_dict = {
        '/index/': index,
        '/ac/': ac
    }


# 响应函数
def run(environ, response):
    """
    :param environ: 接受请求相关的所有数据 wsgiref模块将http请求封装成字典类型
    :param response: 响应数据
    :return: 返回客户端的数据 以列表的形式返回
    """
    # 响应数据 传入响应状态码、响应头
    response('200 OK', [])
    # 获取请求的url
    url = environ['PATH_INFO']
    # 定义一个变量作为程序的标志
    msg = 1
    # 循环遍历url对应关系的字典
    for i in url_dict:
        # 判断获取到到数据是否等于请求的url
        if i == url:
            # 调用url对应的功能函数
            response_data = url_dict[i](url)
            msg = 0
    # 判断是否有对应url响应数据
    if msg:
        response_data = b'404 not found'
    # 将获取到的数据响应到浏览器中
    return [response_data]


if __name__ == '__main__':
    # 实例化 创建服务端对象 实时监听请求
    client = make_server('127.0.0.1', 10086, run)
    # 启动服务端
    client.serve_forever()
