import requests
from lxml import etree
from pymysql import connect


class Spider():
    def __init__(self):
        self.url = 'http://www.hnbitebi.com/hlist-7-1.html'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        self.connect = connect(
            user='root',
            password='rootbxml',
            host='127.0.0.1',
            port=3306,
            database='qinghua',
            charset='utf8'
        )
        self.cs = self.connect.cursor()

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.text

    def parse_data(self, data):
        xml = etree.HTML(data)
        title_links = xml.xpath('//ul[@class="list2"]/li//a/@href')
        titles = xml.xpath('//ul[@class="list2"]/li//a/text()')
        for title_link, title in zip(title_links, titles):
            contents = self.parse_two_data(title_link)
            self.save_data(title, title_link, str(contents))

    def save_data(self, t, tl, con):
        sql = 'insert into qinghua(qh_title, qh_title_link, qh_contents) values (%s, %s, %s)'
        self.cs.execute(sql, [t, tl, con])
        self.connect.commit()

    def parse_two_data(self, url):
        content_data = self.get_data(url)
        xml = etree.HTML(content_data)
        contents = xml.xpath('//div[@class="con"]//p/text()')
        return contents

    def run(self):
        for i in range(1, 44):
            url = 'http://www.hnbitebi.com/hlist-7-{}.html'.format(i)
            data = self.get_data(url)
            self.parse_data(data)
            print('第{}页'.format(i))


if __name__ == '__main__':
    s = Spider()
    s.run()
