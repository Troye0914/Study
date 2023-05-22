import requests
from lxml import etree
from Chaojiying_Client import Chaojiying_Client


class Spider():
    def __init__(self):
        # 首页接口
        self.index_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
        # 用户登录接口
        self.url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
        self.data = {
            '__VIEWSTATE': 'wWCFB0YQAQfRrCt2lJruzPn0oXNETEY842WU5CDN/cCZ/e7lhYgT36Msb4ktSMvkMLPo3FpbWVbDyOtrHxPo7aou8przCWxzQXmWKJ4HT2gbNXhXRJHgEaHduAxVZyPa7r3swg6/nElLTJ8JXjUOmTnqzWE=',
            '__VIEWSTATEGENERATOR': 'C93BE1AE',
            'from': 'http://so.gushiwen.cn/user/collect.aspx',
            'email': '1219246435@qq.com',
            'pwd': 'Nfj-R9b4',
            'code': '',
            'denglu': '登录'
        }
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        self.s = requests.session()  # 实例化session对象

    # 向首页发起请求
    def post_index(self):
        r = requests.get(self.index_url, headers=self.headers)
        html_data = r.text
        xml = etree.HTML(html_data)
        img_src = 'https://so.gushiwen.cn' + xml.xpath('//img[@id="imgCode"]/@src')[0]

        # 将图片保存到本地
        img_data = self.s.get(img_src, headers=self.headers).content
        with open('code.png', 'wb') as f:
            f.write(img_data)

        # 识别验证码
        chaojiying = Chaojiying_Client('Troye0914', 'c!C@h*23', '948255')
        im = open('code.png', 'rb').read()
        return chaojiying.PostPic(im, 1004)['pic_str']

    # 向登录接口发起请求
    def post_user(self):
        result = self.post_index()
        self.data['code'] = result
        r = self.s.post(self.url, headers=self.headers, data=self.data)


if __name__ == '__main__':
    a = Spider()
    a.post_user()
