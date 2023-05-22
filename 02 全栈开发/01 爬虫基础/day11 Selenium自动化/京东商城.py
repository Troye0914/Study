import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Jd(object):
    def __init__(self):
        self.url = 'https://www.jd.com/'
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 创建Chrome浏览器驱动对象
        self.browser = webdriver.Chrome(options=self.options)
        # 用json存储数据
        self.shop_data = {}
        # 页码
        self.index_page = 1
        # 商品编号
        self.index_info = 1

    def get_jd(self):
        # 1.访问站点
        self.browser.get(self.url)

        # 2.等待搜索框出现
        wait = WebDriverWait(self.browser, 30)
        wait.until(EC.presence_of_all_elements_located((By.ID, 'key')))

        # 3.获取搜索框
        text_input = self.browser.find_element(By.ID, 'key')

        # 4.输入内容
        text_input.send_keys('零食')

        # 5.获取并点击搜索按钮
        button = self.browser.find_element(By.CLASS_NAME, 'button')
        button.click()

        # 6.等待页面加载完成
        time.sleep(2)

        while True:
            print('正在爬取第{}页'.format(self.index_page))

            # 7.下拉滑块到底部，刷新内容
            self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

            # 8.等待页面加载完成
            time.sleep(1.5)

            # 9.爬取数据
            data = self.browser.page_source
            self.parse_data(data)

            # 10.等待翻页按钮出现
            wait = WebDriverWait(self.browser, 30)
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'pn-next')))

            try:
                # 11.获取并点击翻页按钮
                self.browser.find_element(By.CLASS_NAME, 'pn-next').click()

                # 12.页数加1
                self.index_page += 1

            except Exception as error:
                print(error)
                print('数据爬取完毕')
                break

    def parse_data(self, data):
        soup = BeautifulSoup(data, 'lxml')
        trade_names = soup.select('.gl-i-wrap a em')  # 商品名
        prices = soup.select('.gl-i-wrap .p-price strong i')  # 价格
        shop_names = soup.select('.gl-i-wrap span a')  # 店铺名
        shop_info_all = {}
        self.index_info = 1
        for trade_name, price, shop_name in zip(trade_names, prices, shop_names):
            t = trade_name.get_text().replace('\n', '')
            p = price.get_text()
            s = shop_name.get_text()
            shop_info = {}
            shop_info['商品名字'] = t
            shop_info['价格'] = p
            shop_info['店铺名'] = s
            shop_info_all[self.index_info] = shop_info
            self.index_info += 1
        self.shop_data['第{}页'.format(self.index_page)] = shop_info_all
        with open('shop_data.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.shop_data, ensure_ascii=False))

    def run(self):
        self.get_jd()


if __name__ == '__main__':
    jd = Jd()
    jd.run()
