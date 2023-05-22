import time
from threading import Timer


def fun(name):
    print('子线程开始执行，时间为')
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print(f'{name}真帅')


if __name__ == '__main__':
    print('子线程开始执行前的时间')
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    # 创建定时器对象
    # Timer(定时的参数，任务函数，参数元组)
    t = Timer(4, fun, ('阿宸',))
    t.start()
