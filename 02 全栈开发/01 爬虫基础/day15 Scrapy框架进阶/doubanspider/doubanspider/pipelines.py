# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanspiderPipeline:
    def __init__(self):
        if os.path.exists('douban.json'):
            os.remove('douban.json')
        self.file = open('douban.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        data = dict(item)
        json_data = json.dumps(data, ensure_ascii=False) + ',\n'
        self.file.write(json_data)
        return item

    def __del__(self):
        self.file.close()


class DoubanspiderPipelineSql:
    def __init__(self):
        self.con = pymysql.connect(
            user='root',
            password='rootbxml',
            database='demo',
            charset='utf8'
        )
        self.cs = self.con.cursor()

    def process_item(self, item, spider):
        item = dict(item)
        print(item)
        sql = 'insert into douban(name, content, link, detail) values (%s,%s,%s,%s)'
        try:
            self.cs.execute(sql, [item['name'], item['content'], item['link'], item['detail']])
            self.con.commit()
        except Exception as e:
            print(e)
        return item

    def close_spider(self):
        self.cs.close()
        self.con.close()
