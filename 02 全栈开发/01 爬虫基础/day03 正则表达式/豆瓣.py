import requests
import re
import os

url = 'https://book.douban.com/latest?icn=index-latestbook-all'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=header)
# with open('./new_book.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)

ti = '<li\sclass="media\sclearfix.*?<a\shref="(.*?)".*?class="subject-cover".*?src="(.*?)".*?<a\sclass="fleft"\shref.*?">(.*?)</a>.*?<p class="subject-abstract color-gray">(.*?)</p>'
res = re.findall(ti, response.text, re.S)
os.mkdir('./图片')
for i in res:
    title_link = i[0]
    image_link = i[1]
    title = i[2]
    detail = i[3].strip()
    # print('标题链接', title_link)
    # print('图片链接', image_link)
    # print('标题', title)
    # print('详情', detail)
    head_img = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    response_img = requests.get(image_link, headers=head_img)

    with open(f'./图片/{title}.jpg', 'wb') as g:
        g.write(response_img.content)
