'''
https://uland.taobao.com/sem/tbsearch
'''
import json
import time
import execjs
import Proxies
import requests
from openpyxl import workbook


class Taobao():
    def __init__(self):
        self.url = "https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/"
        self.headers = {
            'cookie': '__wpkreporterwid_=edfb43c1-e53a-4de5-0b68-7068f97f1ad9; cna=ud7EHAawEzECAcpqVogGUs7h; t=7acf1145fbe89796d74cd6c120f6cb99; sgcookie=E100sNJwpcvMOeFWHnpn05rEGtdi3RzDGKXPnap23cAHlNhE5wfd98na8IDzwDK1QNH55oLLvebgcnAaT8p%2F95UVDw%2BbovM5Xz%2FcXD7%2B8vSw7gc%3D; uc3=vt3=F8dCsfAugXtc3rOGfMo%3D&nk2=DlVs5NM%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&id2=UUGgqLewPbI31g%3D%3D; lgc=mee_t; uc4=nk4=0%40DDC3i1NeOwJp87EC7fNFBw%3D%3D&id4=0%40U2OXkqamvGBMFCxvmo1IyWaJp1sA; tracknick=mee_t; _cc_=WqG3DMC9EA%3D%3D; mt=ci=-1_0; thw=cn; lego2_cna=EK5MHKXTRTDE2TPPHHEHMK2Y; xlly_s=1; _m_h5_tk=9b5f6a279c07fa01c0dbbc979c62b4d2_1684293647348; _m_h5_tk_enc=246d91a29f84f69006521634df3635f4; ctoken=dyMIU7lGBlz2VLyB7JaR3Dja; _tb_token_=e5a7ea3333e63; uc1=cookie14=Uoe8jgqDxYmzuQ%3D%3D; tfstk=cK8hBBw5XOwbhPuJCp_IRtZeVCnAZnFNpLJB7bfOq1UyJeTNi_Ea0sIEjODjLu1..; l=fBjtpEm4Nu8FqD4yBOfZPurza77OSIRYiuPzaNbMi9fPOXCH5dTCW1Z8gN8MC3GVFsZ2R3R4Lnf6BeYBcQAonxvtNSVsr4DmnmOk-Wf..; isg=BEREMUct_FP8RkhG_m17P5dFFcQ2XWjHlR0sbV7l0I_SieRThm04V3orySFRqaAf',
            'referer': 'https://uland.taobao.com/',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        self.params = {}
        self.proxies = Proxies.proxies
        # 用excel存储数据
        self.wb = workbook.Workbook()
        self.ws = self.wb.active

    def get_params(self, page):
        timestamp = str(int(time.time() * 1000))
        data = str({"pNum":page,"pSize":"60","variableMap":"{\"q\":\"连衣裙\",\"navigator\":false,\"recoveryId\":\"201_33.8.7.44_29728858_1684228894734\"}","qieId":"36308","spm":"a2e0b.20350158.31919782","app_pvid":"201_33.8.7.44_29728858_1684228894734","ctm":"spm-url:a2e0b.20350158.31919782.1;page_url:https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Fspm%3Da2e0b.20350158.31919782.1%26pnum%3D1"})
        params = {
            'jsv': '2.5.1',
            'appKey': '12574478',
            't': timestamp,
            'sign': self.get_sign(timestamp, data),
            'api': 'mtop.alimama.union.xt.en.api.entry',
            'v': '1.0',
            'AntiCreep': 'true',
            'timeout': '20000',
            'AntiFlood': 'true',
            'type': 'jsonp',
            'dataType': 'jsonp',
            'callback': 'mtopjsonp2',
            'data': data
        }
        return params

    def get_sign(self, timestamp, data):
        d_token = self.get_d_token()
        i = timestamp
        g = '12574478'
        c_data = data
        sign = self.h(d_token + '&' + i + '&' + g + '&' + c_data)
        return sign

    def get_d_token(self):
        data = self.headers['cookie'].split(';')
        cookie_dict = {}
        for i in data:
            dict_key = i.split('=')[0].strip()
            dict_value = i.split('=')[1]
            cookie_dict[dict_key] = dict_value
        d_token = cookie_dict['_m_h5_tk'].split('_')[0]
        return d_token

    @staticmethod
    def h(data):
        with open('./taobao.js', 'r') as f:
            code = f.read()
        js = execjs.compile(code)
        return js.call('h', data)

    def get_data(self):
        self.ws.append(['商品名', '价格'])
        for page in range(0, 5):
            print('正在爬取第{}页'.format(page + 1))
            self.params = self.get_params(page)
            response = requests.get(self.url, headers=self.headers, params=self.params, proxies=self.proxies)
            json_data = json.loads(response.text[12:-1])
            result_list = json_data['data']['recommend']['resultList']
            for result in result_list:
                name = result['itemName']
                price = result['price']
                row = [name, price]
                self.ws.append(row)
                self.wb.save('./taobao_data.xlsx')

    def run(self):
        self.get_data()


if __name__ == '__main__':
    taobao = Taobao()
    taobao.run()
