import time
import gevent
from gevent import monkey

monkey.patch_all()


def eat(name):
    print(f'{name}在吃炸串')
    time.sleep(2)
    print(f'{name}还在吃炸串')


def sleep(name):
    print(f'{name}在睡觉')
    time.sleep(4)
    print(f'{name}还在睡觉')


if __name__ == '__main__':
    # 创建协程对象
    e = gevent.spawn(eat, '阿宸')
    s = gevent.spawn(sleep, '张三')
    # 用join来开启
    e.join()
    s.join()
