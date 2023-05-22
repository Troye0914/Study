import time
import json
import multiprocessing
from multiprocessing import Process, Lock

multiprocessing.set_start_method('fork')


# 查看数据，票数
def search(name):
    time.sleep(1)
    res = json.load(open('db.txt', 'r', encoding='utf-8'))
    print(f'{name}正在查看票源，当前剩余票数为{res["count"]}')


# 买票
def get(name):
    # 获取当前的数据
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
    # 加锁
    l.acquire()  # 加锁之后一次只能访问一个进程，当这个锁被释放的时候，其他进程才可以陆续进来
    search(name)
    get(name)
    l.release()


if __name__ == '__main__':
    # 创建锁对象
    l = Lock()
    for i in range(10):
        p = Process(target=func, args=('墨离',))
        p.start()
