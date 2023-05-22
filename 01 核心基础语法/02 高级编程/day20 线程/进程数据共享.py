import time
import json
from multiprocessing import Process


# 查看数据，票数
def search(name):
    time.sleep(1)
    res = json.load(open('db.txt', 'r', encoding='utf-8'))
    print(f'{name}正在查看票源，当前剩余票数为{res["count"]}')


# 买票
def get(name):
    # 获得到当前的数据
    res = json.load(open('db.txt', 'r', encoding='utf-8'))
    # 判断数据是否大于0，大于就可以购买
    if res["count"] > 0:
        res["count"] -= 1
        time.sleep(2)
        print(f'{name}购票成功')
        json.dump(res, open('db.txt', 'w', encoding='utf-8'))
    else:
        print(f'今天没有余票，{name}购票失败')


def func(name):
    search(name)
    get(name)


if __name__ == '__main__':
    for i in range(10):
        p = Process(target=func, args=(f'Tom{i}号',))
        p.start()
