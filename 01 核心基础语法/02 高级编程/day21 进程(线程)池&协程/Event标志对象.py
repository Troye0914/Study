import time
import random
from threading import Thread, Event


# 红绿灯
def func_a():
    while True:
        # 让任务恢复成阻塞状态
        e.clear()
        print('红灯')
        time.sleep(4)
        # 将程序设置成非阻塞
        e.set()
        print('绿灯')
        time.sleep(3)


# 行人过马路
def func_b(name):
    while True:
        # 判断程序是否为阻塞的（阻塞——红灯，非阻塞——绿灯）
        if e.is_set():
            print(f'{name}行人正在通行')
            break
        else:
            print(f'{name}行人正在等待')
            e.wait()


if __name__ == '__main__':
    # 创建Event对象
    e = Event()
    # 设置红绿灯启动的线程
    t = Thread(target=func_a)
    t.start()

    # 设置行人的线程
    for i in range(25):
        # 行人到红绿灯的路口情况
        time.sleep(random.randint(0, 3))
        p = Thread(target=func_b, args=(f'{i}号',))
        p.start()
