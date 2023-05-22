import json
import requests
from jsonpath import jsonpath


class Crawler(object):
    tunnel = "a130.kdltps.com:15818"
    username = "t16908862605129"
    password = "zxcv6789"

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
        self.headers['Accept-Encoding'] = 'gzip'
        self.proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": Crawler.username, "pwd": Crawler.password, "proxy": Crawler.tunnel},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": Crawler.username, "pwd": Crawler.password, "proxy": Crawler.tunnel}
        }

    def get_data(self):
        response = requests.get(self.url, headers=self.headers, proxies=self.proxies)
        return response

    def parse_data(self):
        data_text = self.get_data().text
        data_json = json.loads(data_text[14:-1])
        titles = jsonpath(data_json, '$..title')
        tlinks = jsonpath(data_json, '$..tlink')
        for title, tlink in zip(titles, tlinks):
            print(title)
            print(tlink)
            print('======')

    def run(self):
        for i in range(1, 6):
            self.url += '/?callback=data_callback' if i == 1 else f'_0{i}/?callback=data_callback'
            self.parse_data()
            break


if __name__ == '__main__':
    url = 'https://news.163.com/special/cm_yaowen20200213'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'referer': 'https://news.163.com/',
        'cookie': '__bid_n=18704af036054abd334207; _ntes_nuid=73503f772bd73287aa6a79460d797174; s_n_f_l_n3=4e260591d84965bb1683632455309; _antanalysis_s_id=1683632455704; FPTOKEN=pMe8Ykz0K595AJzU4fVomBtlHy583xljAhTwLFQ6tXAdeExS+FhMreVUAuPQEEYMyoxLqGkaagNY60pEZLAegRv4bhLNsaPI5fV9f4qPpnyWugOz4dPOKp3x67/BIxzjPoQXLi01GUQMd8d2lHhFC/oF+ODtz6PeUX+vmwtGyfToE6/QnzTXAs5KUERr7eQB4+t1AVxTmYifBhH1o3dqY/kYas+UT4vPtuhUa6F/159Ncm6C7Y6Nh2msmQsJk+2XTFm+jO6Hg5Ds7WRGicpAW9tbj57oS0/mau2d3HKxmQ2UxU2lcwtHqQ6442RJOzGIwBPCMWYXWYgrMkWD2uFNR2DfF0tcB/kIHW1kb5cCqEvSZyNCwvbMTqiSBDH0f70TlYiRVactJMRNSfRIAOD59Q==|+WE8JPfIsiUa/3tL2enI+O66N8Dz8JHDdjp93n1OGto=|10|2fad27fbbfa019b9762bb156bb69289f; ne_analysis_trace_id=1683634592760; vinfo_n_f_l_n3=4e260591d84965bb.1.0.1683632455309.0.1683634592825'
    }
    craw = Crawler(url, headers)
    craw.run()
