import pymysql
from jinja2 import Template
from wsgiref.simple_server import make_server


def index(url):
    with open('index.html', 'r', encoding='utf-8') as f:
        data = f.read()
    return bytes(data.encode('utf-8'))


def get_data(url):
    user_data = {'name': '阿宸', 'age': 26}
    with open('get_dict.html', 'r', encoding='utf-8') as f:
        data = f.read()
    '''
    通过Jinja2模块，将html读取出来的数据使用模版进行处理，将html文件转化之后也可以使用类似后端语言处理数据
    '''
    temp = Template(data)
    # 将字典数据传递到前端页面中，用键值对的方式进行数据传递
    # 会返回一个接收到后端数据的前端页面
    res = temp.render(user=user_data)
    return bytes(res.encode('utf-8'))


def get_db(url):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='rootbxml',
        charset='utf8',
        database='webdata'
    )
    # 以字典的形式获取数据
    cur = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'select * from user'
    cur.execute(sql)
    data_dict = cur.fetchall()
    with open('get_db.html', 'r', encoding='utf-8') as f:
        data = f.read()
    temp = Template(data)
    res = temp.render(data_list=data_dict)
    return bytes(res.encode('utf-8'))


# 函数与url的对应关系
url_dict = {
    '/index/': index,
    '/get/': get_data,
    '/get_db/': get_db
}


def run(environ, response):
    response('200 OK', [])
    # 根据不同的url后缀（路由）去响应对应功能函数
    url = environ['PATH_INFO']
    msg = 1
    # 遍历字典，获取url对应的函数
    for i in url_dict:
        if i == url:
            response_data = url_dict[i](url)
            msg = 0
    if msg:
        response_data = b'404 not found'
    print(response_data)
    return [response_data]


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8087, run)
    httpd.serve_forever()
